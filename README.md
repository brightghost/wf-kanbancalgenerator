# wf-kanbancalgenerator
Utility to generate formatted calendar lists for Workflowy-like organizers

Note: despite the name, there's nothing really Kanban-specific about the generated calendar lists. Inspired by (WorkFlowy Academy | The Kanban Calendar)[https://www.youtube.com/watch?v=cPkWhwv3KMU].

Sample of the format:

*2019*
*November*
	*_#11-25 Mon_*
	*_#11-26 Tue_*
	*_#11-27 Wed_*
	*_#11-28 Thu_*
	*_#11-29 Fri_*
	*_#11-30 Sat_*
*December*
	*_#12-1 Sun_*
	*_#12-2 Mon_*
	*_#12-3 Tue_*
	*_#12-4 Wed_*
	*_#12-5 Thu_*
	*_#12-6 Fri_*


Usage:

                ./kanban-generator.py
                    Default: generate 12 month's of formatted calendar from today's date

                ./kanban-generator.py 2020-2-5
                    Generate a formatted calendar starting at today's date and ending at the provided date

                ./kanban-generator.py 2020-2-5 2020-2-28
                    Generate a formatted calendar encompassing the start and end dates provided.

                ./kanban-generator.py (-h|--help)
                    Print this usage information and exit

                
