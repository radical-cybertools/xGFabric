
Package radical.template
========================

This Python package represents a template for new radical python projects.  It
will place python modules into the `radical` namespace.  It provides an
installer, testing stubs, module stubs, and a Makefile which supports the most
common activities.   A Makefile is also used to customize this template to
a specific project name.


License
-------

This software is released under the
[LGPL License v3.0](http://opensource.org/licenses/LGPL-3.0).


Usage
-----

* copy or clone this template into a fresh directory
* call `NAME=my_module make templatize`


How it works:
-------------

This repository comes with a make files `Makefile` and a set of files which are
templatized.  The first Makefile will apply a module name to those templates,
this converting this code tree into a viable, installable and testable python
module.  This is done by calling:

```
  NAME=violet make templatize
```

The example invocation above would morph the current file hierarchy in this
directory into a python module named `radical.violet`.

Note that the call to `make templatize` will (re)move the original git
repository, so that the slate is clean for setting up the module's actual git
origin.  It will also remove the Makefile itself.

