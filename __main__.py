from include import *

welcome_message:str = open("./static/welcome.md",mode="r").read()
is_root:bool=os.geteuid() == 0

menus=[
    ["SnapShot Manager - Welcome","welcome-window"],
    ["SnapShot System","snapshot"],
    ]

class InfinitySnapshotManager(App):
    CSS="""
    Header{
        align:center top;
    }
    Tabs#menu-tab{
        width:100%;
        height:3;
        margin-top:0;
    }
    Container{
        width:100%;
        height:auto;
    }
    Static.h1{
        border:heavy white;
    }
    """
    ENABLE_COMMAND_PALETTE=False
    BINDINGS = [
      ("q", "quit_app()", "Quit the application"),
      ]
    def on_mount(self) -> None:
        # Initialize the theme
        infinite_theme = Theme(
            name="infinite",
            primary="#999999",
            secondary="#3333FF",
            accent="#11FFFF",
            foreground="#EEEEEE",
            background="#111111",
            success="#00FFFF",
            warning="#FFFF00",
            error="#FF0000",
            surface="#000000",
            panel="#333333",
            dark=True,
            variables={
                "block-cursor-text-style": "none",
                "footer-key-foreground": "#00ffff",
            },
        )
        # Register the theme
        self.register_theme(infinite_theme)
        self.theme = "infinite"
        # Add Menus
        menu_tab=self.query_one("#menu-tab")
        for menu in menus:
            menu_tab.add_tab(menu[0])
    def compose(self) -> ComposeResult:
        # Compose the UI
        yield Header("The Infinity's SnapShot Manager")
        yield Tabs(id="menu-tab")
        with Container(id=menus[0][1], classes="window"):
            yield Markdown(welcome_message)
        with Container(id=menus[1][1], classes="window"):
            yield Static("SnapShots",classes="h1")
        yield Footer()
    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        if event.tabs.id=="menu-tab":
            """Swap Container"""
            tab_text=event.tab.label
            target_id=""
            for menu in menus:
                if menu[0] == tab_text:
                    target_id=menu[1]
            for container in self.query("Container.window"):
                if container.id==target_id:
                    container.styles.display="block"
                else:
                    container.styles.display="none"
    def on_button_pressed(self, event:Button.Pressed) -> None:
        pass
    def action_quit_app(self):
        self.exit(0)
# Run the application
if __name__ == "__main__":
    if not is_root:
        print("Warning:")
        print("This App must be run as root.")
        sleep(1)
    app = InfinitySnapshotManager()
    app.run()
