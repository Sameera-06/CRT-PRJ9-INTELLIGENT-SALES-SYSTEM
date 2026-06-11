import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df):
    try:
        # Validate input
        if df is None or df.empty:
            print("Error: DataFrame is empty or None")
            return False
        
        # Check required columns
        required_columns = ["Product", "Revenue", "Profit"]
        if not all(col in df.columns for col in required_columns):
            print(f"Error: Missing required columns. Need: {required_columns}")
            return False
        
        # Create reports directory if it doesn't exist
        os.makedirs("reports", exist_ok=True)
        
        pdf = SimpleDocTemplate(
            "reports/Sales_Report.pdf"
        )

        styles = getSampleStyleSheet()

        elements = []

        title = Paragraph(
            "AI Intelligent Sales Report",
            styles["Title"]
        )

        elements.append(title)

        elements.append(
            Spacer(1,12)
        )

        revenue = df["Revenue"].sum()
        profit = df["Profit"].sum()

        summary = Paragraph(
            f"""
        Total Revenue : ₹{revenue:,.0f}<br/>
        Total Profit : ₹{profit:,.0f}<br/>
        Total Orders : {len(df)}
        """,
            styles["BodyText"]
        )

        elements.append(summary)

        elements.append(
            Spacer(1,12)
        )

        table_data = [
            [
                "Product",
                "Revenue",
                "Profit"
            ]
        ]

        product_summary = (
            df.groupby("Product")
            .agg({
                "Revenue":"sum",
                "Profit":"sum"
            })
            .reset_index()
        )

        for _,row in product_summary.iterrows():

            table_data.append([
                row["Product"],
                int(row["Revenue"]),
                int(row["Profit"])
            ])

        table = Table(table_data)

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.gold
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )
            ])
        )

        elements.append(table)

        pdf.build(elements)
        print("✓ PDF report generated successfully: reports/Sales_Report.pdf")
        return True
    
    except Exception as e:
        print(f"Error generating PDF report: {str(e)}")
        return False