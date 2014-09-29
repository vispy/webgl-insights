# Big Data Visualization with WebGL: from Python to JavaScript

Authors: Cyrille Rossant, Almar Klein, Luke Campagnola, Eric Larson, Nicolas Rougier, Kenneth D. Harris

Here is the abstract proposal (deadline October 15).

This is a graphics book for graphics/rendering communities, used to C++ and JavaScript rather than Python. Therefore, we should focus on 1) the OpenGL techniques for big data visualization, and/or 2) how we convert visualizations from Python to JavaScript/WebGL (detailing the different techniques).

## Overview

1. Need to visualize large volumes of data: emphasize on *scalability*, *speed*, and *interactivity* for data exploration.

2. We developed specific techniques with OpenGL ES 2.0 to visualize different types of data. This lets us leverage the computational power of GPUs for big data visualization. (no mention of Python at this stage)

	* big scatter plots with point sprites
	* images with contours
	* multichannel digital signals in a single call
	* high-quality polylines with GLSL agg
	* collections system
	* etc.

3. We implemented these techniques in Vispy, a Python library. Python is one of the leading open platforms for scientific data analysis. However, we also want to bring these Python/OpenGL visualizations to the browser thanks to WebGL. The reasons are:

	* Large volumes of data are hard to move (inertia), so scientists want to access their data remotely through the Web browser.
	* Contrary to Python, the Web browser is ideal for sharing data and analysis reports.
	* The state-of-the-art of bringing Python to the browser for interactive data analysis is the IPython notebook. This platform provides a dynamic Web interface to access a Python server remotely. We will leverage part of this platform for Vispy.

4. We use different techniques to migrate OpenGL visualizations from Python to the Web browser:

	* VNC streaming (server-side rendering)
	* OpenGL streaming
	* GLIR
	* static export

