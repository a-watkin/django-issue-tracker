import datetime as dt


from django.shortcuts import render
from .models import Issue


def get_stats(db_obj):
    """
    Helper method for issues that generates statistical data
    based on issue solve time.
    """
    time_d = []
    for x in db_obj:
        if x.solved_at:
            solved_at = x.solved_at.replace(second=0, microsecond=0)
            created_at = x.created_at.replace(second=0, microsecond=0)

            delta_time = abs(solved_at - created_at)
            time_d.append(delta_time)

            if len(time_d) > 1:
                average_timedelta = sum(time_d, dt.timedelta()) / len(time_d)

    stats = {}

    if len(time_d) > 0:
        stats['longest'] = max(time_d)
        stats['shortest'] = min(time_d)
        if len(time_d) == 1:
            stats['average'] = max(time_d)
            print('test')
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
