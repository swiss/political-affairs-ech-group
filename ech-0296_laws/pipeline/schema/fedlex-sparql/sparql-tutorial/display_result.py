def display_result(df):
    html_content = df.to_html(render_links=True, escape=False)
    print(html_content)