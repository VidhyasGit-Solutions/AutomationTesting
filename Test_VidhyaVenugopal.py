import requests
import pytest

API_BASE_URL = "https://api.spaceflightnewsapi.net/v3"

# Test data for the failing test
INVALID_ROUTE = "/space"

# Test cases 1

def test_get_articles():
    response = requests.get(f"{API_BASE_URL}/articles")
    assert response.status_code == 200

# Test cases 2

def test_get_articles_param():
    response = requests.get(f"{API_BASE_URL}/articles/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test cases 3

def test_get_events():
    response = requests.get(f"{API_BASE_URL}/articles/event/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test cases 4

def test_get_latest_blog_event():
    response = requests.get(f"{API_BASE_URL}/blogs/event/1")
    assert response.status_code == 200
    article = response.json()
    assert isinstance(article, list)

# Test cases 5

def test_get_article_count():
    response = requests.get(f"{API_BASE_URL}/articles/count")
    assert response.status_code == 200

# Test cases 6

def test_get_categories():
    response = requests.get(f"{API_BASE_URL}/info")
    assert response.status_code == 200

# Test cases 7

def test_get_reports_count():
    response = requests.get(f"{API_BASE_URL}/reports/count")
    assert response.status_code == 200

# Test cases 8

def test_get_reports():
    response = requests.get(f"{API_BASE_URL}/reports")
    assert response.status_code == 200

# Test cases 9

def test_get_reports_param():
    response = requests.get(f"{API_BASE_URL}/reports/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test cases 10 - Failing Testcase

def test_get_invalid_route():
    response = requests.get(f"{API_BASE_URL}{INVALID_ROUTE}")
    assert response.status_code == 404

# Failing test
def test_failing_test():
    response = requests.get(f"{API_BASE_URL}/articless")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()