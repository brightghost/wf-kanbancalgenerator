# wf-kanbancalgenerator
## v.0.1

Utility to generate formatted calendar lists for Workflowy-like organizers.

Inspired by [WorkFlowy Academy | The Kanban Calendar](https://www.youtube.com/watch?v=cPkWhwv3KMU) and despite the name, there's nothing really Kanban-specific about the generated calendar lists. They should be useful to anyone who uses a manually-populated calendar for task organization in Workflowy or a similar utility that supports formatted text and tags. The utility outputs raw HTML to the console and, on Linux, will copy this HTML to the clipboard in a format that can be pasted with formatting directly into Workflowy.

If I ever get around to it someday I'll re-write this as a browser-based app with support for customizing the output format, but first I need to use it it long enough to convince myself it's useful. :)

Sample of the format:

<ul>
<li><b>2019</b></li>
<li><b>November</b></li>
  <ul>
	<li><b><i>#11-25 Mon</i></b></li>
	<li><b><i>#11-26 Tue</i></b></li>
	<li><b><i>#11-27 Wed</i></b></li>
	<li><b><i>#11-28 Thu</i></b></li>
	<li><b><i>#11-29 Fri</i></b></li>
	<li><b><i>#11-30 Sat</i></b></li>
  </ul>
<li><b>December</b></li>
  <ul>
	<li><b><i>#12-1 Sun</i></b></li>
	<li><b><i>#12-2 Mon</i></b></li>
	<li><b><i>#12-3 Tue</i></b></li>
	<li><b><i>#12-4 Wed</i></b></li>
	<li><b><i>#12-5 Thu</i></b></li>
	<li><b><i>#12-6 Fri</i></b></li>
  </ul>
</ul>

Usage:

                ./kanban-generator.py
                    Default: generate 12 month's of formatted calendar from today's date

                ./kanban-generator.py 2020-2-5
                    Generate a formatted calendar starting at today's date and ending at the provided date

                ./kanban-generator.py 2020-2-5 2020-2-28
                    Generate a formatted calendar encompassing the start and end dates provided.

                ./kanban-generator.py (-h|--help)
                    Print this usage information and exit

                
