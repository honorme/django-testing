from django.http import JsonResponse
from datetime import datetime, timedelta


def get_info(request):
    try:
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        # Get current day and UTC time
        current_day = datetime.utcnow().strftime('%A')
        # utc_time = (datetime.utcnow() + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
        utc_time = datetime.utcnow().isoformat().split('.')[0] + 'Z'

        # GitHub URLs
        github_file_url = 'https://github.com/honorme/django-testing/blob/master/hng_test_one/views.py'
        github_repo_url = 'https://github.com/honorme/django-testing'

        # Prepare response JSON
        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
