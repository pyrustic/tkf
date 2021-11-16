Back to [Modules overview](https://github.com/pyrustic/tkf/blob/master/docs/modules/README.md)
  
# Module documentation
>## tkf.\_\_init\_\_
Tkf entry point
<br>
[classes (2)](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf.__init__/classes.md)


## Classes
```python
class App(object):
    """
    Tkf's entry point.
    This class should be instantiated inside "$APP_DIR/__main__.py".
    """

    def __init__(self):
        """
                
        """

    @property
    def crash_resistant(self):
        """
        Get the crash_resistant boolean value 
        """

    @crash_resistant.setter
    def crash_resistant(self, val):
        """
        Set True to allow the app to crash when an exception is raised 
        """

    @property
    def geometry(self):
        """
        Get the geometry string. 
        """

    @geometry.setter
    def geometry(self, val):
        """
        Set the geometry string. 
        """

    @property
    def resizable(self):
        """
        Get the resizable boolean
        """

    @resizable.setter
    def resizable(self, val):
        """
        Set a boolean to allow the app to resize or not 
        """

    @property
    def root(self):
        """
        Get the main tk root
        """

    @property
    def theme(self):
        """
        Get the theme object. A theme is a subclass of
        themebase.Theme.
        """

    @theme.setter
    def theme(self, val):
        """
        Set the theme object. A theme is a subclass of themebase.Theme.
        
        If you set None, it will invalidate the previous theme.
        
        Don't forget to call the method "restart()" or "start()" to apply the change !
        Remember that "start()" should be called only once !
        """

    @property
    def title(self):
        """
        Get the title of the app
        """

    @title.setter
    def title(self, val):
        """
        Set the title of the app
        """

    @property
    def view(self):
        """
        Get the view object.
        A view should implement "viewable.Viewable"
        """

    @view.setter
    def view(self, val):
        """
        Set a view object. A view should implement "viewable.Viewable".
        If you set None, the previous view will be destroyed.
        The new view will destroy the previous one if there are a previous one.
        
        Note: "val" can be a tkinter object or a callable (if u plan to REFRESH the app)
        that accepts the app reference as argument and returns a view or a tkinter object
        """

    def center(self):
        """
        Center the window
        """

    def exit(self):
        """
        Exit, simply ;-)
        """

    def maximize(self):
        """
        Maximize the window
        """

    def restart(self):
        """
        Call this method to restart the app.
        If you have submitted a new view or a new theme,
        the previous view or theme will be removed and the new one installed
        """

    def start(self):
        """
        Call this method to start the app.
        It should be called once and put on the last line of the file.
        """

    def _apply_config(self):
        """
        
        """

    def _apply_gui_config(self):
        """
        
        """

    def _apply_theme(self, theme):
        """
        
        """

    def _build(self):
        """
        
        """

    def _get_view(self, view):
        """
        
        """

    def _install_view(self, view, is_refresh=False):
        """
        
        """

    def _on_report_callback_exception(self, exc, val, tb):
        """
        
        """

    def _set_title(self):
        """
        
        """

    def _setup(self):
        """
        
        """

```

```python
class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """


    args = <attribute 'args' of 'BaseException' objects>
    
```

