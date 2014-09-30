# Big Data Visualization with WebGL: from Python to JavaScript

Proposal for the [WebGL Insights](http://www.webglinsights.com/) community book.

## Authors

* Cyrille Rossant (University College London)
* Almar Klein ()
* Luke Campagnola ()
* Eric Larson ()
* Nicolas Rougier (INRIA)
* Kenneth D. Harris (University College London)


## Abstract

The deluge of data arising in many disciplines calls for modern, innovative analysis methods. Whereas more and more processes can be automated, human supervision is nevertheless often required at most stages of the analysis pipelines. The primary way humans can apprehend data for explorative analysis is visualization. Effective big data visualization methods have to be interactive, fast, and scalable.

Modern datasets may be large and high-dimensional, thus no static two-dimensional image can possibly convey all relevant information. A common technique is to create *interactive* visualizations, 



* Need to visualize large volumes of data: emphasize on *scalability*, *speed*, and *interactivity* for data exploration.

* We developed specific techniques with OpenGL ES 2.0 to visualize different types of data. This lets us leverage the computational power of GPUs for big data visualization. Very brief mention of the techniques (no mention of Python at this stage):

	* big scatter plots with point sprites
	* images with contours
	* multichannel digital signals in a single call
	* high-quality polylines with GLSL agg

## From Python to WebGL

* We implemented these techniques in Vispy, a Python library. Python is one of the leading open platforms for scientific data analysis. However, we also want to bring these Python/OpenGL visualizations to the browser thanks to WebGL. The reasons are:

	* Large volumes of data are hard to move (inertia), so scientists want to access their data remotely through the Web browser.
	* Contrary to Python, the Web browser is ideal for sharing data and analysis reports.
	* The state-of-the-art of bringing Python to the browser for interactive data analysis is the IPython notebook. This platform provides a dynamic Web interface to access a Python server remotely. We will leverage part of this platform for Vispy.

* We use different techniques to migrate OpenGL visualizations from Python to the Web browser:

	* VNC streaming (server-side rendering)
	* OpenGL streaming
	* GLIR
	* static export

