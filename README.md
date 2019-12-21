# wf-kanbancalgenerator
Utility to generate formatted calendar lists for Workflowy-like organizers

Note: despite the name, there's nothing really Kanban-specific about the generated calendar lists. Inspired by [WorkFlowy Academy | The Kanban Calendar](https://www.youtube.com/watch?v=cPkWhwv3KMU). The utility outputs raw HTML to the console and, on Linux, will copy the html to the clipboard in a format that can be pasted with formatting directly into Workflowy.

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

                
