# User Interface


{{ extra.project }} comes with a simple and intuitive user interface (UI) layout. The UI
is divided into four areas:

1. Navigation Menu - contains different views like tags, users, groups, inbox
2. Search Bar - quick search of any document
3. User Menu - contains user preferences, API tokens and other menu items.
4. Commander Panel - or Commander - area for browsing documents and folders


![ui layout](./user-interface/ui-layout.jpg)


## Dual Panel Mode

Commander (in figure 1. marked with number 4.) is designed to have
similar look and feel of modern desktop file browsers. This is the place
where you browse your documents and folders.

In order to assist you to quickly move around documents, folders and pages -
there is a special mode - *dual panel model*. In dual panel mode there
are two panels displayed side by side. Between two panels documents (as well
as folders and pages) can be moved with one simple drag'n drop. Figure
below shows how dual panel mode looks like:


![dual panel mode](../img/user-manual/ui/ui-dual-panel-mode.svg)

In order to switch to dual panel mode, use Commander's upper right button:

![switch to dual panel mode](../img/user-manual/ui/switch-to-dual-panel-mode.svg)


To switch back to single panel mode, use close button - which is in the upper right
corner of one of the panels:


![close right panel](../img/user-manual/ui/close-right-panel.svg)

!!! note

        Close button will be displayed only on one of the panels.
        Although both panels look and feel exactly the same, internally
        application still distinguishes them as main and secondary one. Main panel
        is the one which is always visible and secondary panel is the on which
        opens and closes i.e. the one with "close button" in upper right corner.


## Commander


Commander or Commander Panel is one of the two available panels. Commander is
the panel which shows documents and folders - modern web based file browser if
you will.

![commander](../img/user-manual/ui/one_commander.svg)

![two commanders](../img/user-manual/ui/two_commanders.svg)


## Viewer

Viewer or Viewer Panel or Document Viewer is one of the two available panels.
Viewer is the panel in which document is opened.


![one viewer](../img/user-manual/ui/one_viewer.svg)


There can be two Viewers opened side by side. This mode (i.e. dual panel mode
with a Viewer in each panel) is very handy when it comes to moving
pages between documents.

![two viewers](../img/user-manual/ui/two_viewers.svg)


## Thumbnails Panel

Document viewer features a thumbnails panel which can be toggles on and off.
Pages can be selected only inside thumbnails panel; also pages can be
dragged/dropped only from thumbnails panel.


![thumbnails panel](../img/user-manual/ui/thumbnails_panel.svg)


## Context Menu and its Peculiarities


Context menu - is a gui menu which appears when you
perform a right-click operation with your mouse. Context menu appears in same
position where your mouse pointer is when you perform right-click.

{{ extra.project }} features its own context menu,
which may be invoked only when your mouse pointer hovers over Commander or
Viewer. Web browser feature their own context menu - in this sense, browsers'
context menu will appear whenever you perform right-click operation outside
of Commander or Viewer.

Pay attention to the animated image below, the {{ extra.project }} specific context menu
will appear only when you right-click over Commander or Viewer, otherwise the
default browser's built in context menu will be displayed:


![context menu](../img/user-manual/ui/context-menu-only-over-view-or-commander.gif)


Context menu is dynamic - which means that it will display different menu items
depending on what makes sense in current situation. For example, if you did not
select any document or folder then it does not make sense to display menu items such
as "Rename", "Download", "Move" - and context menu won't show those items.

A less obvious, but extremely important to understand, is the fact that
context menu is bound to its panel, in other words if there are two panels
(e.g. two Commander panels) opened side by side, then each panel has its own
instance of context menu. This fact can be illustrated when in one Commander
panel you select one (or multiple) folder(s) - while in other you don't
select anything; in this case, each panel's context menu items will differ:

![context menu bound to panel](../img/user-manual/ui/context-menu-bound-to-panel.gif)

!!! warning

    Context menu is bound to its panel! If there are two panels
    e.g. two Commander panels, then there are two different instances of the
    context menus, and each instance is bound to, in other words is specific
    to, its own Commander.
