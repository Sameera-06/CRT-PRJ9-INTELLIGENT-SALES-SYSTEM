def reorder_point(
avg_demand,
lead_time,
safety_stock
):

    return (
        avg_demand *
        lead_time +
        safety_stock
    )