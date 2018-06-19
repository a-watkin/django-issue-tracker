import datetime as dt


from django.shortcuts import render
from .models import Issue
# Create your views here.


def get_stats(db_obj):
    time_d = []
    for x in db_obj:
        if x.solved_at:
            solved_at = x.solved_at.replace(second=0, microsecond=0)
            created_at = x.created_at.replace(second=0, microsecond=0)

            delta_time = abs(solved_at - created_at)
            time_d.append(delta_time)

            timedeltas = [time_d[i-1]-time_d[i] for i in range(1, len(time_d))]

            if len(time_d) > 1:
                average_timedelta = abs(sum(timedeltas, dt.timedelta(0)) / len(timedeltas))

    stats = {}

    if len(time_d) > 0:
        stats['longest'] = max(time_d)
        stats['shortest'] = min(time_d)
        if len(time_d) == 1:
            stats['average'] = max(time_d)
        else:
            stats['average'] = average_timedelta
    else:
        stats['longest'] = 'Not enough data'
        stats['shortest'] = 'Not enough data'   
        stats['average'] = 'Not enough data'

    return stats


def issues(request):
    issues = Issue.objects.order_by('created_at')

    stats = get_stats(issues)

    return render(request, 'issues.html', {'issues': issues, 'stats': stats})
