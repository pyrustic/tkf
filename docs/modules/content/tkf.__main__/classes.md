Back to [Modules overview](https://github.com/pyrustic/tkf/blob/master/docs/modules/README.md)
  
# Module documentation
>## tkf.\_\_main\_\_
No description
<br>
[functions (1)](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf.__main__/functions.md) &nbsp;.&nbsp; [classes (1)](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf.__main__/classes.md)


## Classes
```python
class Hello(viewable.Viewable):
    """
    Graphical equivalent of a Hello World
    """

    def __init__(self, app):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
        """

    def _build(self):
        """
        This method is part of the view lifecycle
        """

    def _on_click_btn_crash(self):
        """
        
        """

    def _on_click_btn_max(self):
        """
        
        """

    # inherited from viewable.Viewable
    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    # inherited from viewable.Viewable
    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

```

