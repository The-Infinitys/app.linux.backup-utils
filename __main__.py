from include import *

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
        menus=["SnapShot Manager - Welcome","Update System","SnapShot System","Edit SnapShot"]
        menu_tab=self.query_one("#menu-tab")
        for menu in menus:
            menu_tab.add_tab(menu)
    def compose(self) -> ComposeResult:
        # Compose the UI
        yield Header("The Infinity's SnapShot Manager")
        yield Tabs(id="menu-tab")
        yield Footer()
    def action_quit_app(self) -> None:
        self.exit(0)

# Run the application
if __name__ == "__main__":
    euid = os.geteuid()
    if euid!=0:
        print("This App must be run as root.")
        sys.exit(1)
    app = InfinitySnapshotManager()
    app.run()
