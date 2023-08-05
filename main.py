from dash import Dash, html


def main() -> None:
    app = Dash()
    app.title = "Pharama Dashboard"
    app.layout = html.Div()
    app.run()


if __name__ == "__main__":
    main()


