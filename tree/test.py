# Complete the worstPerformingStock function below.
def get_performance(start,end):
    return float((end-start)/start)
def worstPerformingStock(prices):
    worstID=0
    worstPerf = None
    if len(prices)==0:
        return 0
    for item in prices:
        perf = get_performance(item[1],item[0])
        if not worstPerf:
            worstPerf=perf
            worstID=item[0]
        if perf<worstPerf:
            worstID=item[0]
            worstPerf=perf
    
    return worstID
