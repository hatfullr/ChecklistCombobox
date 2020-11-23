# ChecklistCombobox

This widget is a regular ttk.Combobox, but instead of a Listbox in the popdown
window, there is a list of checkboxes. It is designed to function almost
identically to a ttk.Combobox, except for some fringe cases. Learning from
mistakes made in tkinter, this widget is fully customizable to the extent that
tkinter allows.

## Install
To install, you can either download checklistcombobox.py and place it in your
current working directory, or you can do,
```
pip install ChecklistCombobox
```

## Description

The standard Listbox widget from ttk.Combobox is unfortunately inseparable from
the popdown menu because a majority of the tcl code for ttk.Combobox would need
to be replaced. This would mangle any other regular ttk.Combobox widgets
attached to the Tk() instance. Instead, we simply put stuff on top of the
Listbox.

Here is a tree of widgets that are accessible to the user. Tree depth indicates
widget stacking. For example, ChecklistCombobox.popdown is a subwidget (child)
of ChecklistCombobox.
```
Tree                                              Widget type
 ChecklistCombobox                                 ttk.Combobox
	ChecklistCombobox.popdown                      tk.Toplevel
	   ChecklistCombobox.popdown_frame             special popdown frame widget
		  ChecklistCombobox.listbox                tk.Listbox
		  ChecklistCombobox.scrollbar              ttk.Scrollbar
		  ChecklistCombobox.canvas                 tk.Canvas
			 ChecklistCombobox.checkbutton_frame   tk.Frame
				ChecklistCombobox.checkbuttons     list with length = len(values)
				   tk.Checkbutton
```
Any of these widgets can be accessed by the user by simply calling them. For
example, to change the height of all the checkbuttons, you can do,
```
cb = ChecklistCombobox(root,values=('1','2','3','4'))
for button in cb.checkbuttons:
	button.configure(height=2)
```
Equivalently, you can do,
```
cb = ChecklistCombobox(root,values=('1','2','3','4'))
cb.configure(checkbutton_height=2)
```
This is because this class handles the configure method in a special way. The
keywords are parsed and then passed to the appropriate widgets based on the
prefix they are given. Supported prefixes are,
```
popdown_
popdown_frame_
scrollbar_
canvas_
checkbutton_frame_
checkbutton_
checkbutton_selected_
```
Prefix `checkbutton_selected_` can be used to specify the Checkbutton attributes
when they are highlighted, but only the `background`, `foreground`,
`selectcolor`, `activeforeground`, and `activebackground`.
Be careful when using `popdown_frame_` and `scrollbar_` because they are special 
widgets exclusive to the Combobox Popdown menu. You can list their options by 
doing `print(cb.popdown_frame.configure())`. All other prefixes work in the way 
you would expect. Given some option X from the tkinter widget documentation, you 
can change the option using,
```
ChecklistCombobox.configure(prefix_X)
```
You can even configure the checkbuttons separately by giving an array-like
(`list`, `tuple`, or `numpy.ndarray`) argument where the elements have the same
order as the `values` keyword.

So as to avoid confusion, the original ttk.Combobox tcl source code which this
code was based on has been included at the bottom of this code.

Also near the bottom of this code is a short test program you can use simply by
running `python checklistcombobox.py`.
