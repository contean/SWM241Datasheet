.. vim: syntax=rst

SLCD控制模块（SLCD）
--------------

概述
~~

SWM241系列所有型号SLCD控制模块操作均相同，使用前需使能SLCD控制模块时钟, 并通过设置PA15输出高电平开启SLCD电源域。

特性
~~

-  LCD帧频率设置

-  4 COM*32 SEG

-  BIAS和DUTY设置

-  根据图形显示数据，产生驱动电平控制时序

-  本模块仅支持TYPEB驱动波形

-  支持按键扫描功能

模块结构框图
~~~~~~

|SLCD控制002|

图 6‑65 SLCD控制模块结构框图

功能描述
~~~~

本模块为SLCD控制器模块。模块支持标准APB总线操作，只支持WORD读写。

LCD显示
^^^^^

-  配置LCDC_CR寄存器

   -  CLKDIV：指示系统高频频率分频

   -  KEYSCAN：LCD按键扫描

   -  DRIVSEL：LCD驱动电流

   -  SCANFRQ：LCD帧频率

   -  DUTY：LCD扫描模式

   -  BIAS：LCD偏压

   -  DISP：LCD显示模式

   -  DRIVEEN：LCD驱动使能

-  配置LCD显示数据寄存器

-  配置LCDC_CR寄存器

   -  SCANEN：LCD扫描使能

按键扫描
^^^^

LCD驱动端口如果和IO端口复用，可以通过按键扫描功能来配合GPIO端口实现组合按键，同时不影响LCD驱动显示。当按键扫描功能控制位使能后，所有复用端口的波形都会在每个COM开始的时候出现一个约30us宽度的低脉冲；此脉冲可以用作IO中断唤醒信号。

使用软件实现按键扫描功能的步骤如下：

-  把GPIO设置为输入端口，并使能上拉；

-  启动GPIO中断功能；

-  启动按键扫描功能；

-  等待按键；

-  当有按键按下时，系统进入GPIO中断处理子程序：

   -  设置LCD为显示空白状态，并取消按键扫描功能；

   -  设置IO为IO功能，并输出按键探测信号；

   -  读取GPIO端口，判断按键；

   -  设置IO为LCD驱动，并启动LCD显示；

驱动波形
^^^^

表格 6‑4 1/3 BIAS Driver Output Levels

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 0


   * - Driver
     - Mode
     - Alternation
     - Output Level

   * - COMMON
     - Selected
     - H
     - VDD

   * -
     -
     - L
     - GND

   * -
     - Non-Selected
     - H
     - 2*VDD/3

   * -
     -
     - L
     - VDD/3

   * - SEGMENT
     - Selected
     - H
     - VDD

   * -
     -
     - L
     - GND

   * -
     - Non-Selected
     - H
     - 2*VDD/3

   * -
     -
     - L
     - VDD/3


|SLCD控制003|

图 6‑66 1/4DUTY和1/3BIAS驱动模式波形

|SLCD控制004|

图 6‑67 1/3DUTY和1/3BIAS驱动模式波形

表格 6‑5 1/2 BIAS Driver Output Levels

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 0


   * - Driver
     - Mode
     - Alternation
     - Output Level

   * - COMMON
     - Selected
     - H
     - VDD

   * -
     -
     - L
     - GND

   * -
     - Non-Selected
     - H
     - VDD/2

   * -
     -
     - L
     - VDD/2

   * - SEGMENT
     - Selected
     - H
     - VDD

   * -
     -
     - L
     - GND

   * -
     - Non-Selected
     - H
     - VDD

   * -
     -
     - L
     - GND


|SLCD控制005|

图 6‑68 1/3DUTY和1/2BIAS驱动模式波形

数据显示映射表
^^^^^^^

表格 6‑6 显示数据映射表

.. list-table::
   :widths: 16 16 16 16 16 16
   :header-rows: 0


   * -
     - SEG0
     - SEG1
     - ……
     -
     -

   * - COM0
     - LCDC _DATA0/B0
     - LC DATA0/B1
     - ……
     - LC DAT B30
     - LC DAT B31

   * - COM1
     - LCDC _DATA1/B0
     - LC DATA1/B1
     - ……
     - LC DAT B30
     - LC DAT B31

   * - COM2
     - LCDC _DATA2/B0
     - LC DATA2/B1
     - ……
     - LC DAT B30
     - LC DAT B31

   * - COM3
     - LCDC _DATA3/B0
     - LC DATA3/B1
     - ……
     - LC DAT B30
     - LC DAT B31


寄存器映射
~~~~~

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 名称   |
     - | 偏移 |
     - |
       |
        |
        |
     - |

        |
        |
     - 描述                       | | | |

   * - SLCDBASE：0 |x400A9800
     - |
     -
     -
     -

   * - CR
     - 0x00
     -
     - 0x F0000
     - SLCD配置寄存器             |

   * - DATA0
     - 0x10
     -
     - 0x 00000
     - SLCD数据寄存器0            |

   * - DATA1
     - 0x14
     -
     - 0x 00000
     - SLCD数据寄存器1            |

   * - DATA2
     - 0x18
     -
     - 0x 00000
     - SLCD数据寄存器2            |

   * - DATA3
     - 0x1c
     -
     - 0x 00000
     - SLCD数据寄存器3            |


寄存器描述
~~~~~

SLCD控制寄存器CR
^^^^^^^^^^^

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 寄存器 |
     - | 偏移 |
     - |
       |
         |
     - 复位值 |    描 | |
     - |
            |
              |

   * - CR
     - 0x00
     -
     - 0 3F0000
     - SLCD配置寄存器             |


.. list-table::
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 0


   * - 31
     - 30
     - 29
     - 28
     - 27
     - 26
     - 25
     - 24

   * - -
     -
     -
     -
     -
     -
     -
     -

   * - 23
     - 22
     - 21
     - 20
     - 19
     - 18
     - 17
     - 16

   * - -
     -
     - CL K_DIV
     -
     -
     -
     -
     -

   * - 15
     - 14
     - 13
     - 12
     - 11
     - 10
     - 9
     - 8

   * - -
     -
     -
     -
     -
     - K EYSCAN
     - -
     -

   * - 7
     - 6
     - 5
     - 4
     - 3
     - 2
     - 1
     - 0

   * - SCANFRQ
     -
     - DUTY
     - BIAS
     - DISP
     -
     - S CANEN
     - DRIVEN


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - 位域 |
     - 名称     | |
     - 描述                                        | |

   * - 31:22
     - -
     - -

   * - 21:16
     - CLKDIV
     - 系统分频控制                                |

       Flcd = PCLK2 / (CLKDIV*32)

       注：由                                      | CD模块挂载在APB2总线上，APB2总线时钟(PCLK  | 系统时钟(SYSCLK)的二分频，故PCLK2=SYSCLK/2 |

   * - 15:11
     - -
     - -

   * - 10
     - KEYSCAN
     - 按键扫描功能                                |

       1使能                                       |

   * - 9:8
     - -
     - -

   * - 7:6
     - SCANFRQ
     - LCD帧频率控制                               |

       00：Flcd/256 Hz                             |

       01：Flcd/128 Hz                             |

       10：Flcd/64 Hz                              |

       11：Flcd/32 Hz                              |

   * - 5
     - DUTY
     - LCD扫描模式选择                             |

       0：1/4 Duty                                 |

       1：1/3 Duty                                 |

   * - 4
     - BIAS
     - LCD偏压模式选择                             |

       0：1/3 Bias                                 |

       1：1/2 Bias                                 |

   * - 3:2
     - DISP
     - LCD显示模式                                 |

       00：正常显示                                |

       01：显示空白                                |

       10：显示全部                                |

       11：保留                                    |

   * - 1
     - SCANEN
     - LCD扫描电路使能                             |

       0：不使能                                   |

       1：使能                                     |

   * - 0
     - DRIVEN
     - LCD驱动电路使能                             |

       0：不使能                                   |

       1：使能                                     |


SLCD数据寄存器0 DATA0
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 寄存器 |
     - | 偏移 |
     - |
       |
         |
     - 复位值 |    描 | |
     - |
            |
              |

   * - DATA0
     - 0x10
     -
     - 0 000000
     - SLCD数据寄存器0            |


.. list-table::
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 0


   * - 31
     - 30
     - 29
     - 28
     - 27
     - 26
     - 25
     - 24

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 23
     - 22
     - 21
     - 20
     - 19
     - 18
     - 17
     - 16

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 15
     - 14
     - 13
     - 12
     - 11
     - 10
     - 9
     - 8

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 7
     - 6
     - 5
     - 4
     - 3
     - 2
     - 1
     - 0

   * - DATA
     -
     -
     -
     -
     -
     -
     -


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - 位域 |
     - 名称     | |
     - 描述                                        | |

   * - 31:0
     - DATA0
     - LCD数据寄存器0                              |


SLCD数据寄存器1 DATA1
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 寄存器 |
     - | 偏移 |
     - |
       |
         |
     - 复位值 |    描 | |
     - |
            |
              |

   * - DATA1
     - 0x14
     -
     - 0 000000
     - SLCD数据寄存器1            |


.. list-table::
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 0


   * - 31
     - 30
     - 29
     - 28
     - 27
     - 26
     - 25
     - 24

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 23
     - 22
     - 21
     - 20
     - 19
     - 18
     - 17
     - 16

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 15
     - 14
     - 13
     - 12
     - 11
     - 10
     - 9
     - 8

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 7
     - 6
     - 5
     - 4
     - 3
     - 2
     - 1
     - 0

   * - DATA
     -
     -
     -
     -
     -
     -
     -


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - 位域 |
     - 名称     | |
     - 描述                                        | |

   * - 31:0
     - DATA1
     - LCD数据寄存器1                              |


SLCD数据寄存器2 DATA2
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 寄存器 |
     - | 偏移 |
     - |
       |
         |
     - 复位值 |    描 | |
     - |
            |
              |

   * - DATA2
     - 0x18
     -
     - 0 000000
     - SLCD数据寄存器2            |


.. list-table::
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 0


   * - 31
     - 30
     - 29
     - 28
     - 27
     - 26
     - 25
     - 24

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 23
     - 22
     - 21
     - 20
     - 19
     - 18
     - 17
     - 16

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 15
     - 14
     - 13
     - 12
     - 11
     - 10
     - 9
     - 8

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 7
     - 6
     - 5
     - 4
     - 3
     - 2
     - 1
     - 0

   * - DATA
     -
     -
     -
     -
     -
     -
     -


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - 位域 |
     - 名称     | |
     - 描述                                        | |

   * - 31:0
     - DATA2
     - LCD数据寄存器2                              |


SLCD数据寄存器3 DATA3
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 0


   * - 寄存器 |
     - | 偏移 |
     - |
       |
         |
     - 复位值 |    描 | |
     - |
            |
              |

   * - DATA3
     - 0x1c
     -
     - 0 000000
     - SLCD数据寄存器3            |


.. list-table::
   :widths: 12 12 12 12 12 12 12 12
   :header-rows: 0


   * - 31
     - 30
     - 29
     - 28
     - 27
     - 26
     - 25
     - 24

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 23
     - 22
     - 21
     - 20
     - 19
     - 18
     - 17
     - 16

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 15
     - 14
     - 13
     - 12
     - 11
     - 10
     - 9
     - 8

   * - DATA
     -
     -
     -
     -
     -
     -
     -

   * - 7
     - 6
     - 5
     - 4
     - 3
     - 2
     - 1
     - 0

   * - DATA
     -
     -
     -
     -
     -
     -
     -


.. list-table::
   :widths: 33 33 33
   :header-rows: 0


   * - 位域 |
     - 名称     | |
     - 描述                                        | |

   * - 31:0
     - DATA3
     - LCD数据寄存器3                              |


.. |SLCD控制002| image:: media\SLCD控制002.emf
.. |SLCD控制003| image:: media\SLCD控制003.emf
.. |SLCD控制004| image:: media\SLCD控制004.emf
.. |SLCD控制005| image:: media\SLCD控制005.emf
