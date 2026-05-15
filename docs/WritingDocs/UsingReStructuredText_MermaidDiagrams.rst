.. _rst-diagrams-ref:

Using reStructuredText - Mermaid diagrams
*********************************************

The sphinxcontrib-mermaid_ extension allows you to embed Mermaid_ graphs in your documents, including general flowcharts, sequence diagrams, gantt diagrams and more.

It adds a directive to embed mermaid markup. 


Class diagrams
=================

Refer to https://mermaid.ai/open-source/syntax/classDiagram.html for the full syntax.

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
        +name: String
        +age: Integer
        +isMammal() Boolean
        +mate()
    }

    class Duck {
        +beakColor: String="yellow"
        +swim()
        +quack()
    }

    class Fish {
        -sizeInCentimetre: Integer
        -swim()
    }

    class Zebra {
        +isWild: Boolean
        +run()
    }

.. _block_end_202602251652:

...is created by this block of code:

.. literalinclude:: UsingReStructuredText_MermaidDiagrams.rst
   :start-after: block_begin_202602251652
   :end-before: block_end_202602251652

Sequence diagrams
=================
 
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

.. literalinclude:: UsingReStructuredText_MermaidDiagrams.rst
   :start-after: block_begin_202602251651
   :end-before: block_end_202602251651



.. links-placeholder

.. include:: ../_sharedFiles/Links.rst