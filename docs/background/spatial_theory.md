# Space Syntax 理论笔记

> 目标：给 survey 的非建筑学读者一个够用、可计算、可迁移的 Space Syntax primer。  
> 用途：支撑 `survey_plan_v4.md` 的 Phase 0 readiness gate，并作为后续 `L0-L5` taxonomy 与 research agenda 的理论桥。

---

## 1. 为什么这套理论对本 survey 重要

Space Syntax 的核心不是“空间长什么样”，而是“空间各部分如何彼此关联”。  
它关心的不是单个房间、走廊或街道本身，而是这些空间在整体布局中的相对位置关系，以及这种关系如何改变：

- 人会遇到谁
- 人更可能走哪里
- 哪些位置更公开，哪些位置更私密
- 哪些位置更像中介、门户、门槛或瓶颈

对本 survey 而言，这一点非常关键。我们讨论的不是 LLM agent 会不会“看见 3D 世界”，而是：

> 当 agent 接收到的空间信息从地点名称，提升到邻接关系、共在关系、构型指标甚至几何约束时，社会行为是否会随之变化？

所以，Space Syntax 为这篇 survey 提供的不是一个“建筑学背景知识包”，而是一套可以把“空间”转成结构化变量的框架。

---

## 2. 配置不是拼图：Configuration vs. Composition

Space Syntax 最重要的起点，是区分 `composition` 和 `configuration`。

### 2.1 Composition

Composition 关注空间元素本身的局部属性，例如：

- 房间大小
- 形状
- 门窗数量
- 装饰风格
- 功能标签

这些属性当然重要，但它们还不能说明“这个空间在整体里处于什么位置”。

### 2.2 Configuration

Configuration 关注的是：

- 一个空间到其他空间有多深
- 是否必须穿过它才能到达别处
- 它与多少空间直接相连
- 它在整体网络里是偏中心还是偏边缘

换句话说，configuration 研究的是：

> 一个空间由于嵌入整体关系网络而获得的性质。

这正是本 survey 想借到 LLM agent 文献里的部分。  
如果一个 agent 只知道“酒吧”“公园”“家”，它拿到的是 `composition-like labels`。  
如果它还知道“酒吧连接多个公共路径”“公园可见性高”“某房间深度高且私密”，它才开始接触 `configuration-like structure`。

---

## 3. 空间如何被表示成图

Space Syntax 的很多分析都可以写成图论问题。

### 3.1 节点与边

最简单的抽象是：

- 节点：房间、街段、可见位置、轴线，或采样点
- 边：可达、可见、相邻、可穿行等关系

不同表示法会产生不同图：

- `justified graph`: 以一个根节点展开拓扑深度
- `axial graph`: 用最少且最长的可视-可行走线表示布局
- `visibility graph`: 用大量采样点和“互相可见”关系表示开放空间

### 3.2 拓扑距离

在这类图里，最常见的距离不是米数，而是 `topological distance`：

- 两个空间相邻，距离记作 1
- 需要经过 2 个中间层级，距离更深

这与欧氏几何不同。  
一个物理上很近但被多道门隔开的空间，在拓扑上可能很“远”；  
一个物理上并不近但一路通透、连接直接的空间，在拓扑上可能很“近”。

这也是 Space Syntax 对本 survey 的一个重要启发：

> 对社会行为有影响的，不一定是几何距离本身，而可能是 agent 感知到的可达结构、共在机会和通路组织方式。

---

## 4. Justified Graph：如何手算深度结构

`justified graph` 是最适合 Phase 0 建立直觉的工具。

做法很简单：

1. 选一个根节点
2. 根节点放在最上层
3. 与根节点直接相连的空间放在下一层
4. 再往下展开其余空间

它的作用不是画得漂亮，而是让你一眼看出：

- 这个根节点离整体有多近
- 它是否位于中心层级
- 它周围是分散型还是树枝型结构

### 4.1 一个 5 节点例子

设空间图如下：

```text
B - A - D - E
    |
    C
```

节点含义可以想象为：

- `A`: 大厅
- `B`: 小房间 1
- `C`: 小房间 2
- `D`: 过渡走廊
- `E`: 深处房间

#### 以 A 为根

- 到 `B` 的距离 = 1
- 到 `C` 的距离 = 1
- 到 `D` 的距离 = 1
- 到 `E` 的距离 = 2

所以：

- `Total Depth(A) = 1 + 1 + 1 + 2 = 5`
- 系统一共 `k = 5` 个节点
- `Mean Depth(A) = 5 / (5 - 1) = 1.25`

#### 以 B 为根

- 到 `A` 的距离 = 1
- 到 `C` 的距离 = 2
- 到 `D` 的距离 = 2
- 到 `E` 的距离 = 3

所以：

- `Total Depth(B) = 1 + 2 + 2 + 3 = 8`
- `Mean Depth(B) = 8 / 4 = 2`

解释：

- `A` 比 `B` 更浅，更中心
- `B` 更边缘，更私密

这已经足够传达 Space Syntax 最关键的直觉：

> 空间的位置不是“标签属性”，而是整个系统里的关系位置。

---

## 5. 核心指标

### 5.1 Depth

`Depth` 描述一个空间到另一个空间，或到整体空间系统的拓扑层级距离。

- `d(i, j)`: 从节点 `i` 到节点 `j` 的最短拓扑距离
- `TD(i) = sum_j d(i, j)`: 节点 `i` 到其余节点的总深度
- `MD(i) = TD(i) / (k - 1)`: 节点 `i` 的平均深度

直觉上：

- `MD` 越小，节点越接近系统中心
- `MD` 越大，节点越深、越偏、越隔离

### 5.2 Integration

`Integration` 可以理解为“全局可达性”或“拓扑中心性”的 Syntax 版本。

常见写法是先算相对不对称度：

```text
RA(i) = 2 * (MD(i) - 1) / (k - 2)
```

再做系统规模归一化，得到 `RRA`，最后用其倒数表达 integration：

```text
Integration(i) ~ 1 / RRA(i)
```

不同软件和论文会有细微变体，但直觉一致：

- Integration 高：更中心、更容易被到达、更容易成为相遇热点
- Integration 低：更深、更偏、更像退让空间或边缘空间

对 survey 的翻译：

- 如果 agent 拿到的是高 integration 位置提示，它可能更容易预测“这里更公共、更容易发生遭遇”
- 这正对应未来 `L4` 层把构型指标注入 agent 的设想

### 5.3 Connectivity

`Connectivity` 是局部指标，表示一个节点有多少直接邻居。

```text
Connectivity(i) = degree(i)
```

它反映的是局部连通，而不是全局中心性。

一个节点可能：

- connectivity 很高，但在整体上仍然偏边缘
- connectivity 一般，但因为处于系统中央而 integration 很高

因此，connectivity 和 integration 不能混为一谈。

### 5.4 Control Value

`Control Value` 关心一个节点对邻居通行选择的“控制力”。

常见定义为：

```text
CV(i) = sum_{j in N(i)} 1 / degree(j)
```

直觉：

- 如果你的邻居本身选择很少，那么你对它们更重要
- 如果某个空间是多个低连通区域的门槛，它的 control value 往往较高

在上面的例子里：

- `B` 只有一个出口连到 `A`
- `C` 也只有一个出口连到 `A`
- `D` 虽然连到 `A` 和 `E`，但 `E` 只能通过 `D`

所以 `A` 和 `D` 都有一定控制力，但 `A` 对整体更像入口分配点。

对本项目的启发：

- 高 control 节点可能更容易成为守门、协调、拦截、观察他人的位置
- 这与“角色分化”“门槛行为”“信息中介”有直接关系

### 5.5 Choice

`Choice` 接近图论里的 betweenness centrality：

- 统计有多少最短路径经过某节点

直觉：

- 高 choice 的位置不是最中心的“目的地”
- 它更像“经常被路过”的通道或桥梁

如果 integration 更像“你有多容易被到达”，choice 更像“你有多容易被经过”。

对社会行为而言：

- 高 integration 可能对应相遇热点
- 高 choice 可能对应经过流量高、偶遇频繁、监视/展示机会多的通路

### 5.6 Intelligibility

`Intelligibility` 是系统层指标，常写成：

> 局部连通性与全局整合度之间的相关程度

常见做法是看：

- `Connectivity`
- `Integration`

二者在全系统中的相关关系。

如果 intelligibility 高，说明：

- 你只靠局部线索，也更容易推断整体结构

如果 intelligibility 低，说明：

- 你从局部看起来很难猜到整体组织方式

这对 agent 很有意义。  
如果某系统只提供局部观察，而环境本身 intelligibility 很低，agent 可能更难形成稳定的空间行为策略。

---

## 6. Axial Map vs. VGA

### 6.1 Axial Map

Axial map 传统上用“最少且最长的可通视/可通行线”来表示空间骨架。

它特别适合：

- 街道网络
- 走廊主轴
- 以移动路径为主的问题

优点：

- 强调 movement structure
- 便于分析线网络层面的整合与选择

局限：

- 对开放室内空间、广场、复杂视觉场不够细
- 更偏“线”的表示

### 6.2 VGA: Visibility Graph Analysis

VGA 把开放空间采样成大量点：

- 每个点是一个节点
- 如果两点互相可见，就连一条边

这样得到的是 `visibility graph`，而不是单点 isovist。

VGA 的关键进步在于：

- 它把“从某点看得到什么”的局部视域
- 扩展成“整个环境如何被互相看见”的全局结构

它更适合：

- 室内空间
- 视线组织
- way-finding
- 局部可见性如何影响移动与停留

### 6.3 为什么 Turner (2001) 重要

Turner 等人把 Benedikt 的 isovist 思路从局部几何属性推进到图结构层面，提出：

- 单个 isovist 太局部
- 必须看一组点之间的互可见关系
- 才能把视觉结构真正放进 configurational analysis

这对 survey 尤其重要，因为它给出了一条很清楚的桥：

- `L2`: 语义描述
- `L3`: 邻接/共在
- `L4`: 构型指标
- `L5`: 完整几何

其中 `L4` 并不要求 agent 直接“看到 3D 世界”，而是可以先接收由图分析得到的结构指标。

---

## 7. 从公式到直觉：一个最小 worked example

继续用前面的 5 节点图。

### 7.1 深度

- `A` 的 `MD = 1.25`
- `B` 的 `MD = 2`

这说明 `A` 更浅，`B` 更深。

### 7.2 粗略 integration 对比

对于 `k = 5`：

- `RA(A) = 2 * (1.25 - 1) / 3 = 0.167`
- `RA(B) = 2 * (2 - 1) / 3 = 0.667`

即使不继续做 `RRA` 归一化，我们也已经能看出：

- `A` 显著比 `B` 更 integrated

### 7.3 control 对比

各点 degree：

- `deg(A) = 3`
- `deg(B) = 1`
- `deg(C) = 1`
- `deg(D) = 2`
- `deg(E) = 1`

于是：

```text
CV(A) = 1/deg(B) + 1/deg(C) + 1/deg(D)
      = 1 + 1 + 1/2
      = 2.5
```

```text
CV(D) = 1/deg(A) + 1/deg(E)
      = 1/3 + 1
      = 1.333...
```

说明：

- `A` 更像中心分配点
- `D` 更像通往深处房间 `E` 的门槛

### 7.4 行为含义

如果把它翻译成社会行为语言：

- `A` 更适合偶遇、展示、汇合
- `E` 更适合隐私、停留、避开他人
- `D` 更可能承载守门、拦截、通过型接触

这正是 Space Syntax 对本 survey 最有价值的部分：

> 它把“空间影响社会行为”从模糊直觉变成可编码、可比较、可实验化的结构假设。

---

## 8. 对 LLM multi-agent survey 的直接启发

### 8.1 为什么现在的 LLM agent 文献还没真正进入构型层

很多系统已经有“空间”：

- 房间名
- 地点标签
- 2D 或 3D 场景
- 用户位置

但对 agent 来说，常见输入仍然只是：

- “你在厨房”
- “Alice 在客厅”
- “用户正朝你走近”

这些信息可以支持语义化反应，但还不等于构型级空间知识。

### 8.2 `L4` 的真正含义

本 survey 中的 `L4` 不是“更炫的 3D”。

`L4` 指的是：

- agent 明确接收到构型指标
- 例如 integration、depth、choice、control
- 或这些指标的稳定等价物

也就是说，`L4` 是一种“压缩后的结构知识”，而不是原始几何。

这点非常重要，因为它意味着：

- 我们不必等待完美 embodied agent 才能研究空间社会行为
- 只要能把配置结构编码成 agent 可访问输入，就可以开始实证

### 8.3 这也是本 survey 的桥接论点

Foundational corpus 告诉我们：

- 在物理空间里，构型与相遇、移动、占用、边界感相关

Core corpus 目前显示：

- LLM multi-agent 系统大多停留在地点标签、语义描述、有限邻接

Research agenda 因此是：

- 不直接宣称 Space Syntax 命题已经迁移成功
- 而是提出一个可检验设计空间：把构型指标作为 agent 输入，看社会行为是否按理论方向变化

---

## 9. 本 survey 里哪些命题能迁移，哪些还不能

### 可以迁移的是

- “空间结构可以被编码为关系变量”
- “全局拓扑位置与局部行为机会并不等价”
- “公共性、私密性、门槛性可以部分由结构位置解释”

### 不能直接迁移的是

- “人类在建筑中的所有经验规律，会自动复制到 LLM agent”
- “高 integration 一定导致更多社交”
- “control value 一定导致领导者涌现”

对 survey 的标准写法应该是：

> Space Syntax 为 LLM multi-agent systems 提供了可迁移的结构性假设与编码维度，但这些命题在人工智能体社会中的行为效应仍缺乏直接实证。

---

## 10. Phase 0 要记住的最小结论

如果只记住五句话，应该是：

1. Space Syntax 研究的是空间的关系位置，不是局部描述。
2. Integration、Depth、Control、Choice 都是“结构变量”，不是视觉装饰。
3. Axial 分析更偏 movement skeleton，VGA 更偏 visibility structure。
4. `L4` 不等于 `L5`；构型指标输入是一条独立于完整几何的路线。
5. 对本 survey 来说，最重要的不是证明 Space Syntax 已经在 LLM agent 中成立，而是证明它提供了一个尚未被系统探索的 representational design space。

---

## 参考

- Hillier, B., & Hanson, J. (1984). *The Social Logic of Space*.
- Hillier, B. (1996). *Space is the Machine*.
- Turner, A., Doxa, M., O'Sullivan, D., & Penn, A. (2001). *From Isovists to Visibility Graphs*.
- Penn, A., & Turner, A. (2001/2002). *Space Syntax Based Agent Simulation*.
