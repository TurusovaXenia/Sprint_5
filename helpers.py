from datetime import datetime

def generate_email(domain='test.com'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'test_{timestamp}@{domain}'