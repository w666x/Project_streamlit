.. _function_helps:

=================
通用函数手册
=================

.. note::
    * 本节主要介绍常用的函数
    

函数说明
==================================

torch
-------------

.. _torch_gather:

torch.gather
^^^^^^^^^^^^^

* **功能说明**
    * 从原input tensor中获取指定dim和指定index的数据 ``gather(input, dim, index)``

.. code-block:: python
    :linenos:
    
    # 目标tensor如下，维度为`torch.Size([3, 5])`
    >>> import torch
    >>> t = torch.tensor([[ 0.3992,  0.9006,  0.6797,  0.4850,  0.6004],
                      [ 0.0000,  0.2908,  0.0000,  0.4152,  0.0000],
                      [ 0.5735,  0.0000,  0.9044,  0.0000,  0.1732]])
    >>> t.size()
    torch.Size([3, 5])

    # 给定索引如下
    >>> torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]])
    tensor([[0, 1, 2, 0, 0],
            [2, 0, 0, 1, 2]])



1. 给定torch.gather维度为0时，结果为，**即维度为0时，给定的值都是在给维度0赋值**
    - `[0, 1, 2, 0, 0]` 对应的从目标t中取值的索引为， `[0, 0], [1, 1], [2, 2], [0, 3], [0, 4]` , 作为结果表第1行的值哦
    - `[2, 0, 0, 1, 2]` 对应的从目标t中取值的索引为， `[2, 0], [0, 1], [0, 2], [1, 3], [2, 4]` ，作为结果表第3行的值哦

.. code-block:: python
    :linenos:
    
    >>> torch.gather(t, 0, torch.tensor([[0, 1, 2, 0, 0], [0, 1, 2, 0, 0], [2, 0, 0, 1, 2], [2, 0, 0, 1, 2]]))
    tensor([[0.3992, 0.2908, 0.9044, 0.4850, 0.6004],
            [0.3992, 0.2908, 0.9044, 0.4850, 0.6004],
            [0.5735, 0.9006, 0.6797, 0.4152, 0.1732],
            [0.5735, 0.9006, 0.6797, 0.4152, 0.1732]])
    >>> print(t[0, 0], t[1, 1], t[2, 2], t[0, 3], t[0, 4])
    tensor(0.3992) tensor(0.2908) tensor(0.9044) tensor(0.4850) tensor(0.6004)
    >>> print(t[2, 0], t[0, 1], t[0, 2], t[1, 3], t[2, 4])
    tensor(0.5735) tensor(0.9006) tensor(0.6797) tensor(0.4152) tensor(0.1732)


2. 给定torch.gather维度为1时，结果为，**即维度为1时，给定的值都是在给维度1赋值**
    - `[0, 1, 2, 0, 0]` 对应的从目标t中取值的索引为， `[0, 0], [0, 1], [0, 2], [0, 0], [0, 0]` , 作为结果表第1行的值哦
    - `[2, 0, 0, 1, 2]` 对应的从目标t中取值的索引为， `[1, 2], [1, 0], [1, 0], [1, 1], [1, 2]` , 作为结果表第2行的值哦
    - `[2, 0, 0, 1, 2]` 对应的从目标t中取值的索引为， `[2, 2], [2, 0], [2, 0], [2, 1], [2, 2]` , 作为结果表第3行的值哦


.. code-block:: python
    :linenos:
    
    >>> torch.gather(t, 1, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2], [2, 0, 0, 1, 2]]))
    tensor([[0.3992, 0.9006, 0.6797, 0.3992, 0.3992],
            [0.0000, 0.0000, 0.0000, 0.2908, 0.0000],
            [0.9044, 0.5735, 0.5735, 0.0000, 0.9044]])
    >>> print(t[0, 0], t[0, 1], t[0, 2], t[0, 0], t[0, 0])
    tensor(0.3992) tensor(0.9006) tensor(0.6797) tensor(0.3992) tensor(0.3992)
    >>> print(t[2, 2], t[2, 0], t[2, 0], t[2, 1], t[2, 2])
    tensor(0.9044) tensor(0.5735) tensor(0.5735) tensor(0.) tensor(0.9044)




torch.scatter
^^^^^^^^^^^^^

* **功能说明**
    * 通过给定索引，`scatter(input, dim, index, src)` 从src中获取字段，来覆盖input中的值

.. code-block:: python
    :linenos:
    
    # 目标tensor如下，维度为`torch.Size([4, 6])`
    >>> import torch
    >>> t = torch.full((4, 6), 0)
    tensor([[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]])
    >>> t.size()
    torch.Size([4, 6])
    
.. code-block:: python
    :linenos:
    
    # 给定索引如下
    >>> index = torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]])
    tensor([[0, 1, 2, 0, 0],
            [2, 0, 0, 1, 2]])
    # src如下，维度为`torch.Size([2, 5])`
    >>> src = torch.arange(1, 11).reshape((2, 5))
    tensor([[ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10]])

1. 给定torch.scatter维度为0时，结果为，**即维度为0时，给定的值都是在给维度0赋值**
    - src的j列按照index的j列中的值散射到input的j列中；
        - **比如第3列src的值为[3,8], index值为[2,0],则3被赋值给input的第3列index=2位置了； 8被赋值给input第3列的index=0的位置了**
    - `[0, 2]` 对应的是将src中第1列的2个值[1, 6]赋值给目标t下述位置处， `[0, 0], [2, 0]`
    - `[1, 0]` 对应的是将src中第2列的2个值[2, 7]赋值给目标t下述位置处， `[1, 1], [0, 1]`
    - `[2, 0]` 对应的是将src中第3列的2个值[3, 8]赋值给目标t下述位置处， `[2, 2], [0, 2]`

.. code-block:: python
    :linenos:
    
    >>> res = torch.scatter(t, 0, index, src)
    >>> res
    tensor([[ 1,  7,  8,  4,  5,  0],
            [ 0,  2,  0,  9,  0,  0],
            [ 6,  0,  3,  0, 10,  0],
            [ 0,  0,  0,  0,  0,  0]])
    >>> print(res[0, 0], res[1, 1], res[2, 2], res[0, 3], res[0, 4])
    tensor(1) tensor(2) tensor(3) tensor(4) tensor(5)
    >>> print(res[2, 0], res[0, 1], res[0, 2], res[1, 3], res[2, 4])
    tensor(6) tensor(7) tensor(8) tensor(9) tensor(10)


2. 给定torch.scatter维度为1时，结果为，**即维度为1时，给定的值都是在给维度1赋值**
    - src的i行按照index的i行中的值散射到input的i行中
        - **比如第1行src的值为[1,2,3,4,5], index值为[0,1,2,0,0],则3被赋值给input的第1行index=2位置了；5被赋值给input第1行的index=0的位置了，且覆盖了前面被赋值的4**
    - `[0, 1, 2, 0, 0]` 对应的是将src中第1行的5个值赋值给目标t下述位置处， `[0, 0], [0, 1], [0, 2], [0, 0], [0, 0]`
    - `[2, 0, 0, 1, 2]` 对应的是将src中第2行的5个值赋值给目标t下述位置处， `[1, 2], [1, 0], [1, 0], [1, 1], [1, 2]`

.. code-block:: python
    :linenos:
    
    >>> res = torch.scatter(t, 1, index, src)
    >>> res
    tensor([[ 5,  2,  3,  0,  0,  0],
            [ 8,  9, 10,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0]])
    >>> print(res[0, 0], res[0, 1], res[0, 2], res[0, 0], res[0, 0])
    tensor(5) tensor(2) tensor(3) tensor(5) tensor(5)
    >>> print(res[1, 2], res[1, 0], res[1, 0], res[1, 1], res[1, 2])
    tensor(10) tensor(8) tensor(8) tensor(9) tensor(10)

   

torch.unsqueeze 
^^^^^^^^^^^^^^^^
* 返回一个新的张量，对输入的既定位置插入维度 1， ``torch.unsqueeze(input, dim, out=None)``
    * 注意：返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。
    * 如果dim为负，则将会被转化dim+input.dim()+1

.. ipython:: python

    import torch
    x = torch.Tensor([1, 2, 3, 4]) 
    print(x) 
    print(x.size()) 
    print(x.dim()) 
    print(x.numpy()) 
    
    # 在维度0处，新增一个维度
    print(torch.unsqueeze(x, 0)) 
    print(torch.unsqueeze(x, 0).size()) 
    print(torch.unsqueeze(x, 0).dim()) 
    print(torch.unsqueeze(x, 0).numpy())  

    # 在维度1处，新增一个维度
    print(torch.unsqueeze(x, 1))
    print(torch.unsqueeze(x, 1).size())
    print(torch.unsqueeze(x, 1).dim())

    # 在维度-1 + x.shape[0] + 1处，即维度1处新增一个维度
    print(torch.unsqueeze(x, -1))
    print(torch.unsqueeze(x, -1).size())
    print(torch.unsqueeze(x, -1).dim())
    
    # 在维度-2 + x.shape[0] + 1处，即维度0处新增一个维度
    print(torch.unsqueeze(x, -2))
    print(torch.unsqueeze(x, -2).size())
    print(torch.unsqueeze(x, -2).dim())

torch.squeeze
^^^^^^^^^^^^^
* ``torch.squeeze(input, dim=None, out=None)`` 将输入张量形状中的1 去除并返回。 
    * 如果输入是形如(A×1×B×1×C×1×D)，那么输出形状就为： (A×B×C×D)
    * 当给定dim时，那么挤压操作只在给定维度上。
        * 例如，输入形状为: (A×1×B), **squeeze(input, 0) 将会保持张量不变，只有用 squeeze(input, 1)，形状会变成 (A×B)。**
        
.. ipython:: python

    import torch
    m = torch.zeros(2, 1, 2, 1, 2)
    print(m.size())
    n = torch.squeeze(m)
    print(n.size())
    n = torch.squeeze(m, 0)
    print(n.size())
    n = torch.squeeze(m, 1)
    print(n.size()) 
    n = torch.squeeze(m, 2)
    print(n.size()) 
    n = torch.squeeze(m, 3)
    print(n.size())
    p = torch.zeros(2, 1, 1)
    print(p) 

torch.view
^^^^^^^^^^^^^
* 即指定维度后，剩下的维度自动推断

.. ipython:: python

    import torch
    tt1=torch.tensor([-0.3623, -0.6115,  0.7283,  0.4699,  2.3261,  0.1599])
    print(tt1.shape)
    result=tt1.view(3,2)
    print(result.shape)
    tt2=torch.tensor([[-0.3623, -0.6115],
                [ 0.7283,  0.4699],
                [ 2.3261,  0.1599]])
    print(tt2.shape)
    result=tt2.view(2, -1)
    print(result.shape)



torch.clamp
^^^^^^^^^^^^^
* 将input 的值控制在min 和 max 之间
    * torch.clamp(input, min, max, out=None) → Tensor

.. ipython:: python

    import torch
    tt1=torch.tensor([-0.3623, -0.6115,  0.7283,  0.4699,  2.3261,  0.1599])
    print(torch.clamp(tt1, 0, 1))