## ***cyclient.view.get_current***

**`cyclient.view.get_current(self, layout=None, network=None, verbose=False)`**

Returns the current view or null if there is none.

* **`verbose`** print more

* **`returns`** current view or null if there is none

___

## ***cyclient.view.create***

**`cyclient.view.create(self, layout=None, network=None, verbose=False)`**

Creates a new view for the passed network and returns the SUID of the
new view and the original network. If no networks are specified, it
creates a view for the current network, if there is one.

* **`layout (string, optional)`** If true (default), the preferred layout
will be applied to the new view. If false, no layout will be applied.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`** eg. 2123


___

## ***cyclient.view.fit_content***

**`cyclient.view.fit_content(self, verbose=False)`**

Zooms out the current view in order to display all of its elements.

* **`verbose`** print more


___

## ***cyclient.view.update***

**`cyclient.view.update(self, network=None, verbose=False)`**

Sets the current view, which can also be null.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more


___

## ***cyclient.view.list***

**`cyclient.view.list(self, network=None, verbose=False)`**

Returns a list with the passed network's views or an empty list if
there are no views. If a network is not specified, it assumes the
current network.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`** a list with the passed network's views or an empty list if there are no views


___

## ***cyclient.view.export***

**`cyclient.view.export(self, Height=None, options=None, OutputFile=None, Resolution=None, Units=None, Width=None, Zoom=None, view="current", verbose=False)`**

Exports the current view to a graphics file and returns the path to the
saved file. PNG and JPEG formats have options for scaling, while other
formats only have the option 'exportTextAsFont'. For the PDF format,
exporting text as font does not work for two-byte characters such as
Chinese or Japanese. To avoid corrupted texts in the exported PDF,
please set false to 'exportTextAsFont' when exporting networks including
those non-English characters.

* **`Height (string, optional)`** The height of the exported image. Valid
only for bitmap formats, such as PNG and JPEG.
* **`options (string, optional)`** The format of the output file. =
['JPEG (*.jpeg, *.jpg)', 'PDF (*.pdf)', 'PNG (*.png)', 'PostScript (*.ps)',
'SVG (*.svg)']
* **`OutputFile (string, optional)`** The path name of the file where
the view must be saved to. By default, the view's title is used as
the file name.
* **`Resolution (string, optional)`** The resolution of the exported
image, in DPI. Valid only for bitmap formats, when the selected width
and height 'units' is inches. The possible values are: 72 (default),
100, 150, 300, 600. = ['72', '100', '150', '300', '600']
* **`Units (string, optional)`** The units for the 'width' and 'height'
values. Valid only for bitmap formats, such as PNG and JPEG. The
possible values are: pixels (default), inches. = ['pixels', 'inches']
* **`Width (string, optional)`** The width of the exported image. Valid
only for bitmap formats, such as PNG and JPEG.
* **`Zoom (string, optional)`** The zoom value to proportionally scale
the image. The default value is 100.0. Valid only for bitmap formats,
such as PNG and JPEG
* **`view (string, optional)`** Specifies a network view by name, or by 
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank value 
can also be used to specify the current network view.
* **`verbose`** print more

* **`returns`** path to the saved file

___

## ***cyclient.view.destroy***

**`cyclient.view.destroy(self, verbose=False)`**

Destroys all selected network views and returns their SUIDs. If no views
are selected, this command does nothing.

* **`verbose`** print more

* **`returns`** eg. [ 2155 ]

___

## ***cyclient.view.set_current***

**`cyclient.view.set_current(self, network=None, verbose=False)`**

Sets the current view, which can also be null.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more


___

## ***cyclient.view.fit_selected***

**`cyclient.view.fit_selected(self, verbose=False)`**

Changes the current view's zoom and viewport so the selected nodes and
edges fit into the view area.

* **`verbose`** print more


___

