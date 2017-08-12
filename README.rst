This is a workaround to transform a pypiwin32 wheel demand into a pywin32 wheel demand
======================================================================================

A wheel created with this, and placed in the same D:/toto directory as a "pywin32" wheel will make equivalent:: 

  $ pip install pypiwin32 --no-index --trusted-host=None  --find-links=D:/toto

  $ pip install pywin32   --no-index --trusted-host=None  --find-links=D:/toto


Inspiration :
-------------

* pypiwin32 wheel is a workaround to the not available "pip install pywin32" 
 
* This will re-direct packages requiring a "pypiwin32" to a "pywin32" wheel, providing you have one.
 
Thanks :
--------

* Many thanks to Christoph Gohlke for the suggestion.