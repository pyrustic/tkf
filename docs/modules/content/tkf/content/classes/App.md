Back to [All Modules](https://github.com/pyrustic/tkf/blob/master/docs/modules/README.md#readme)

# Module Overview

> **tkf**
> 
> Tkf entry point
>
> **Classes:** &nbsp; [App](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf/content/classes/App.md#class-app) &nbsp; [Error](https://github.com/pyrustic/tkf/blob/master/docs/modules/content/tkf/content/classes/Error.md#class-error)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class App
Tkf's entry point.
This class should be instantiated inside "$APP_DIR/__main__.py".

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|crash_resistant|getter|Get the crash_resistant boolean value ||
|crash_resistant|setter|Set True to allow the app to crash when an exception is raised ||
|geometry|getter|Get the geometry string. ||
|geometry|setter|Set the geometry string. ||
|resizable|getter|Get the resizable boolean||
|resizable|setter|Set a boolean to allow the app to resize or not ||
|root|getter|Get the main tk root||
|theme|getter|Get the theme object. A theme is a subclass of
themebase.Theme.||
|theme|setter|Set the theme object. A theme is a subclass of themebase.Theme.

If you set None, it will invalidate the previous theme.

Don't forget to call the method "restart()" or "start()" to apply the change !
Remember that "start()" should be called only once !||
|title|getter|Get the title of the app||
|title|setter|Set the title of the app||
|view|getter|Get the view object.
A view should implement "viewable.Viewable"||
|view|setter|Set a view object. A view should implement "viewable.Viewable".
If you set None, the previous view will be destroyed.
The new view will destroy the previous one if there are a previous one.

Note: "val" can be a tkinter object or a callable (if u plan to REFRESH the app)
that accepts the app reference as argument and returns a view or a tkinter object||



# All Methods
[\_\_init\_\_](#__init__) &nbsp; [\_apply\_config](#_apply_config) &nbsp; [\_apply\_gui\_config](#_apply_gui_config) &nbsp; [\_apply\_theme](#_apply_theme) &nbsp; [\_build](#_build) &nbsp; [\_get\_view](#_get_view) &nbsp; [\_install\_view](#_install_view) &nbsp; [\_on\_report\_callback\_exception](#_on_report_callback_exception) &nbsp; [\_set\_title](#_set_title) &nbsp; [\_setup](#_setup) &nbsp; [center](#center) &nbsp; [exit](#exit) &nbsp; [maximize](#maximize) &nbsp; [restart](#restart) &nbsp; [start](#start)

## \_\_init\_\_
        



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_apply\_config
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_apply\_gui\_config
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_apply\_theme
No description



**Signature:** (self, theme)



**Return Value:** None

[Back to Top](#module-overview)


## \_build
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_get\_view
No description



**Signature:** (self, view)



**Return Value:** None

[Back to Top](#module-overview)


## \_install\_view
No description



**Signature:** (self, view, is\_refresh=False)



**Return Value:** None

[Back to Top](#module-overview)


## \_on\_report\_callback\_exception
No description



**Signature:** (self, exc, val, tb)



**Return Value:** None

[Back to Top](#module-overview)


## \_set\_title
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## center
Center the window



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## exit
Exit, simply ;-)



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## maximize
Maximize the window



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## restart
Call this method to restart the app.
If you have submitted a new view or a new theme,
the previous view or theme will be removed and the new one installed



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## start
Call this method to start the app.
It should be called once and put on the last line of the file.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)



