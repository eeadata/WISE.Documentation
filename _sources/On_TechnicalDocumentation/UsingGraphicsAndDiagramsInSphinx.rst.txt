:tocdepth: 2

.. highlight:: none

.. metadata-placeholder

   :DC.Title:
   	Creating diagrams
   :DC.Creator:
   	Nery, Fernanda
   :DC.Date:
   	2013-10-01
   :DC.Description:
      Overview of some available alternatives for
      producing and including SVG graphics and UML diagrams in Sphinx.
   :DC.Language:
   	en
   :DC.Format:
   	text/x-rst

.. _rst-diagrams-ref:

Creating diagrams
***************************

.. contents:: On this page...
   :depth: 3
   :local:


Using Mermaid
==============

The sphinxcontrib-mermaid_ extension allows you to embed Mermaid_ graphs in your documents, including general flowcharts, sequence diagrams, gantt diagrams and more.

It adds a directive to embed mermaid markup. 

Sequence diagrams
------------------
 
This sequence diagram...

.. _block_begin_202602251651:

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      participant Charlie
      Alice->Bob: How are you?
      loop Thinking
          Bob->Bob: I need a holiday...
      end
      Note right of Bob: Just reply <br/>something...
      Bob-->Alice: Great!
      Bob->Charlie: How about you?
      Charlie-->Bob: Jolly good!

.. _block_end_202602251651:

...is created by this block of code:

.. literalinclude:: UsingGraphicsAndDiagramsInSphinx.rst
   :start-after: block_begin_202602251651
   :end-before: block_end_202602251651

Class diagrams
------------------

This class diagram...

.. _block_begin_202602251652:

.. mermaid::

   classDiagram
    %% Relationships
    Animal <|-- Duck
    Animal <|-- Fish
    Animal <|-- Zebra

    %% Class Definitions
    class Animal {
        +String name
        +int age
        +isMammal() bool
        +mate()
    }

    class Duck {
        +String beakColor
        +swim()
        +quack()
    }

    class Fish {
        -int sizeInFeet
        -canEat()
    }

    class Zebra {
        +bool is_wild
        +run()
    }

.. _block_end_202602251652:

...is created by this block of code:

.. literalinclude:: UsingGraphicsAndDiagramsInSphinx.rst
   :start-after: block_begin_202602251652
   :end-before: block_end_202602251652


.. links-placeholder

.. include:: ../_sharedFiles/Links.rst