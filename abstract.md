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

The deluge of data arising in many disciplines calls for modern, innovative analysis methods. Whereas more and more processes can be automated, human supervision is nevertheless often required at most stages of the analysis pipelines. The primary way humans can apprehend data for explorative analysis is visualization. Effective big data visualization methods have to be *interactive*, *fast*, and *scalable*.

Modern datasets may be large and high-dimensional, thus no static two-dimensional image can possibly convey all relevant information. A common technique is to create *interactive* visualizations, where the user can explore the various dimensions and subsets of the data. For such data exploration to be most effective, the rendering framerate need to be optimal even with very large datasets. Finally, big data visualization methods need to support distributed and remote technologies in order to scale to huge datasets stored in cloud architectures.

We developed specific rendering techniques with OpenGL ES 2.0 to leverage the computational power of graphics units for interactive big data visualization. We implemented these techniques in a Python library called Vispy. Python is one of the leading open source platforms for data analysis and numerical computing. Whereas there are many visualization and plotting libraries in Python, Vispy is one of the first libraries that lets scientists visualize millions of data points interactively at an optimal framerate. Vispy supports many types of datasets: scatter plots, digital signals, images, 3D models, and many others. Its flexible and layered architecture allows for the creation of custom visuals and rendering techniques like volume rendering or ray tracing. Vispy notably features an object-oriented interface to OpenGL that considerably simplifies the standard OpenGL API for the most common use-cases.

Whereas Python is an excellent platform for data analysis, it lags behind the Web browser when it comes to remote visualization and sharing of interactive analysis reports. The need for remote data access is all the more critical that the size of common datasets increases faster than transfer speeds. Therefore, it is common practice for large datasets to be stored in the cloud, while analysts visualize the data remotely through the Web browser on a desktop or mobile device.

In this chapter, we will present the different techniques we have been developing in order to integrate our OpenGL-based Python library into the Web browser thanks to WebGL. The main challenge is to let scientists visualize their data without having them write any JavaScript code. Most scientists do not have a formal training in programming, and they would be unwilling to learn an additional language beyond Python. Therefore, we are aiming for an automatic and transparent Web backend for Vispy.

The first approach consists of letting the server render the scene locally and send the raster images to the browser in real-time. This technique may be useful on low-end clients.

In the second approach, the server emits OpenGL command calls that are proxied to the Web browser. The browser renders the scene by executing these commands through WebGL. This method may involve transfers of significant volumes of data. However, most of our visualization techniques involve GPU data transfers at initialization time only. This is the main and most useful approach.

In the last approach, the server exports an entire visualization to a standalone interactive HTML/JavaScript document. This method is restricted to relatively simple cases. However, users familiar with JavaScript can extend the exported document through a simple API. This approach is useful when an interactive visualization is needed in absence of a Python server.

The last two approaches feature a new intermediate-level representation of all OpenGL constructs we need in Vispy. A static visualization in this representation is described by a linear sequence of commands that instruct the interpreter to create buffers, define OpenGL programs, and draw the scene. This level of abstraction matches Vispy's object-oriented interface to OpenGL. We needed to define this new representation because the regular OpenGL API was too low-level for our needs.

For interactivity, we developed a combination of Python-to-JavaScript code translation utilities, JavaScript numerical computing libraries, and high-level interactive constructs in order to export a reactive visualization from Python to JavaScript.

All of these approaches are useful in different use-cases.


## Screenshots

TODO: a few screenshots

> A few examples of scientific visualizations with Vispy. A. A simple example illustrating the use of vertex and fragment shaders. B. Scatter plot with point sprites. C. High-performance multi-channel digital signal viewer: all signals are rendered with a single OpenGL API call. D. Graph rendering. E. 3D mesh of a brain. F. Visualization of thousands of molecules with the technique of fake impostors (each atom is point sprite rendered with a fragment-shader-based ray tracing implementation).
