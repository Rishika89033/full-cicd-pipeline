def test_website_content():
    with open("index.html", "r") as file:
        content = file.read()

    assert "Welcome to My CI/CD Website" in content
