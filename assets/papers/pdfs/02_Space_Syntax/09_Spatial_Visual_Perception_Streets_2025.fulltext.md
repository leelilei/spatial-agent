Title: ﻿Evaluation of spatial visual perception of streets based on deep learning and spatial syntax

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/02_Space_Syntax/09_Spatial_Visual_Perception_Streets_2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:06:50+00:00
- page_count: 15
- status: ok
- text_char_count: 67980

Metadata:
- author: unknown
- doi: 10.1038/s41598-025-03189-z
- keywords: unknown
- subject: unknown

Outline:
- ﻿Evaluation of spatial visual perception of streets based on deep learning and spatial syntax (page 1)
  - ﻿Literature review (page 2)
    - ﻿Traditional street quality study (page 2)
    - ﻿Street quality research incorporating big data (page 2)
    - ﻿Street quality research based on big data and artificial intelligence (page 3)
  - ﻿Materials and methods (page 4)
    - ﻿Study area (page 4)
    - ﻿Research framework (page 5)
      - ﻿Constructing street view image dataset (page 5)
      - ﻿Deep learning based semantic segmentation of street view images (page 5)
      - ﻿Perceptual scoring of street view images using a Human- machine adversarial scoring framework (page 6)
      - ﻿Street accessibility analysis and combined street quality portfolio analysis (page 8)
  - ﻿Analysis of results (page 9)
    - ﻿Analysis of street view image components (page 9)
    - ﻿Analysis of visual perception of streets based on BSVI (page 9)
    - ﻿Multiple regression analysis of visual perception and visual elements (page 10)
    - ﻿Overlay analysis of street accessibility and street quality (page 11)
  - ﻿Conclusion (page 12)
  - ﻿References (page 13)

Markdown Content:

www.nature.com/scientificreports
OPEN Evaluation of spatial visual
perception of streets based on
deep learning and spatial syntax
Mingyang Yu1, Xin Chen1, Xiangyu Zheng1, Weikang Cui1,2, Qingrui Ji1 & Huaqiao Xing1
Street visual quality improvement plays an important role in urban development. An important
direction for street quality research lies in accurately perceiving the spatial quality of urban streets and
exploring the connection with street constituents. This study applies deep learning to extract visual
elements from street view images and uses a human-machine adversarial model to rate them across
six dimensions (beautiful, wealthy, safety, lively, depressing, and boring). Through spatial visualization
of street quality, overlay analysis with network accessibility, and multiple linear regression, it
examines the correlations between street space quality and its constituent elements. The results
indicate that the streets within the study area scored highly on the dimensions of beautiful and lively,
this is attributed to the reasonable greening construction which characterized by the good layout
and density of greenery. Such greening not only enhances aesthetics but also provides environmental
benefits. Additionally, the orderly street layout reflects well-organized spatial arrangements of street
elements, such as pathways and building facades. Positive visual perception such as beautiful, wealthy,
safety, lively is positively correlated with plants and pedestrians, and negatively correlated with
walls. It is important to address the distinct types of streets in urban planning, including high-quality/
accessibility streets found in urban centers, high-quality/low-accessibility streets at district junctions
with sparse networks, low-quality/high-accessibility streets in the southwestern center and Low-
quality/accessibility peripheral areas characterized by outdated buildings. Strategies should prioritize
improvements in street function, greening, building interfaces, and pedestrian connectivity. These
measures will help enhance the overall spatial quality and vitality of the area. In summary, the findings
provide data support for more precise urban street improvements and offer a reference for human-
centered urban planning research.
Keywords Deep learning, Street images, Spatial syntax, Urban planning
Streets are essential public spaces for urban residents, providing a physical and social environment for
daily interactions and recreation1. As vital connectors between people and the city, streets shape residents’
experiences, influencing mobility, safety, social interaction, and overall urban life. City managers increasingly
focus on street design to enhance socio-economic and cultural activities, aiming to create more sustainable,
livable environments2. City managers are paying increasing attention to the design and planning of urban
streets as important hubs of socio-economic and cultural activities. A deep understanding of the intricate
relationship between the components of urban streets and human perception is conducive to a harmonious and
sustainable urban environment. Traditionally, planners and designers relied on labor-intensive methods such
as on-site surveys or static maps, which provided limited insights into the visual and spatial qualities of streets.
Inadequate technology for large-scale data processing and a lack of comprehensive data sources have hindered
the development of scientific and rational street planning blueprints.
The emergence of streetscape imagery has overcome the previous limitations on the availability of data
sources for assessing streets3,4. Streetscape images are electronic maps based on actual landscapes, and these
maps provide richly detailed streetscape images with a wide range of coverage containing a large amount of
information about city streets5,6. Therefore, these street view images have the potential to become an important
form of supporting data for assessing the visual perception of city streets. Currently, a number of Internet
companies such as Google, Microsoft, Baidu, and Tencent have launched online street view services7,8. In China,
Baidu Maps’ online Street View service already covers a large number of streets in most cities.
1School of Surveying and Geo-Informatics, Shandong Jianzhu University, Jinan 250101, China. 2Inspur Smart City
Technology Co., Ltd, Jinan 250014, China. email: ymy@sdjzu.edu.cn
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 1

www.nature.com/scientificreports/
As a new data source, Street View images have gradually become a research hotspot. A large number of urban
studies based on Street View images include 3D city reconstruction studies9,10, specific scene recognition11,
perceptual safety assessment12, alcohol consumption data extraction13, assessment of visual perception of
streets14, and other related areas. Among them, visual perception of streets is the basis for exploring urban
planning and quality of life of residents15. Meanwhile, with the advancement in the field of computers, it is now
possible to utilize convolutional neural networks for fast and accurate fine-grained processing of street images.
This technique can effectively recognize various elements such as buildings, roads, pedestrians, and greenery16.
Through the combination of deep learning technology and streetscape images, it can provide refined basic data
for the study of street spatial quality, and at the same time, it can quickly process large-scale data, making it
technically possible to quickly and accurately measure the visual quality of streets on a large scale.
However, current research still falls short in revealing the quantitative relationship between street components
and human subjective perception, lacking both systematic approaches and scalability. Consequently, an urgent
research gap exists regarding how to combine emerging large-scale street view data and deep learning technologies
to achieve high-precision, wide-coverage measurement of street visual quality. Against this backdrop, this study
endeavors to bridge the aforementioned gap: on the one hand, advanced methods such as deep learning and
space syntax are employed to comprehensively quantify street visual quality and its constituent elements; on the
other hand, subjective perception dimensions are integrated with objective quantitative metrics to systematically
evaluate how the street environment influences residents’ daily lives and urban development. This integration
enhances our understanding of the intricate relationship between street visual characteristics and residents’
experiences, thereby offering more targeted optimization strategies for urban planning and decision-making.
In this study, considering the subjective feelings of people who are the main users of streets and the objective
physical characteristics of streets, an efficient evaluation model of urban street visual quality is constructed by
using multi-source big data such as street view images and OSM street vector data, combined with deep learning,
spatial syntax and Random Forest model. It can be used for large-scale and high-detailed evaluation of the visual
quality of urban streets to better provide reference for urban planning assessment and assisted decision-making,
as well as the improvement of the quality of the human environment.
Literature review
Traditional street quality study
The study of street space quality has its roots in the 1960s, with seminal contributions from urban theorists
such as JACOBS J and LEFEBVRE H, who emphasized the human-scale perspective in urban design. Jacobs,
in her work The Death and Life of Great American Cities (1961), critiqued the separation of functions in cities
and argued that the vitality of streets is directly linked to their ability to support diverse, pedestrian-friendly
environments17. Lefebvre, in The Production of Space (1974), introduced the idea that the spatial organization
of cities is a socially constructed phenomenon, influencing both daily life and urban interactions18. These early
studies laid the groundwork for understanding the importance of human-scale urban design, focusing on the
street as a space of social interaction and pedestrian use.
Building on these foundations, Kevin Lynch’s influential book The Image of the City (1960) further explored
the way individuals perceive and experience urban spaces. Lynch’s work emphasized the concept of “imageability”
and how streets contribute to the legibility and identity of cities19. His framework categorized urban spaces into
elements such as paths, edges, districts, nodes, and landmarks, providing a systematic approach for evaluating
street spaces from a psychological and sensory perspective.
As urban studies progressed, research on street quality expanded to cover various types of urban
environments, including commercial districts20, public squares21, and residential streets22. For example, studies
have highlighted the role of pedestrian-friendly streets in enhancing social interaction and contributing to the
economic vitality of city centers. In contrast, other research has examined the impact of traffic congestion, safety,
and environmental factors on the perceived quality of streets in residential areas23. These studies have revealed
that street quality is a multifaceted concept, encompassing physical, social, and psychological dimensions.
Over the past few decades, there has been a marked shift towards more objective and systematic methods of
street quality evaluation. Traditional approaches, which relied heavily on manual measurement and subjective
assessment, often faced challenges in scalability and precision. For instance, methods such as surveys and
visual inspections were limited by researcher biases and logistical constraints, making large-scale and detailed
assessments of street quality difficult to conduct. In response to these limitations, there has been a growing trend
toward integrating quantitative techniques into street quality analysis24.
One significant milestone in the development of quantitative methods for street evaluation was the introduction
of spatial syntax in 1984 by Bill Hillier and Julienne Hanson25. Spatial syntax focuses on the topological properties
of street networks, enabling researchers to quantify and visualize accessibility, connectivity, and movement
patterns within urban spaces. This approach provides valuable insights into the structural organization of streets,
as well as their potential for fostering social interactions and facilitating efficient transportation. Today, spatial
syntax remains an essential tool in urban planning and design, with applications ranging from large-scale city
planning to micro-level pedestrian movement analysis26.
Street quality research incorporating big data
The rapid advancement of computer technology has greatly expanded the ways in which urban street quality
can be analyzed. The diversification of data collection methods, particularly with the introduction of Point of
Interest (POI) data, has enabled more comprehensive and precise quantitative evaluations of street spaces. POI
data, which captures locations of notable urban features such as shops, public facilities, and cultural landmarks,
has proven especially useful in urban studies. Zhang et al. (2019) leveraged POI data and public awareness tasks
to map the accuracy of POI data to the linear space of streets, creating a detailed method for classifying street
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 2

www.nature.com/scientificreports/
types based on urban functions and use patterns27. This approach marked a significant step in fine-grained
street quality assessment, allowing for a more nuanced understanding of how different types of streets serve
their surrounding communities. Similarly, Liu et al. (2021) used POI data to analyze the relationship between
urban street characteristics and economic activity, showing how street designs influence commercial vitality
in urban areas28. Qin et al. (2020) explored the relationship between street vitality and urban data in tourist
cities, combining POI data with Baidu heat maps and OpenStreetMap (OSM) road network data. Their study
offered insights into how different types of urban spaces, such as tourist districts, are shaped by the dynamics of
human activity and transportation networks29. Such studies show how big data can not only support basic spatial
assessments but also provide dynamic metrics for understanding the vitality and usage patterns of streets in real
time. Additionally, Zhao et al. (2021) extended this analysis by incorporating weather and traffic data, showing
that street vitality in tourist districts is highly sensitive to external factors such as weather conditions and public
transport availability30.
As the availability of data sources has grown, quantitative measurement techniques for street quality have
become increasingly diverse. Geographic Information Systems (GIS) remain one of the most widely adopted
methods, offering powerful tools for spatial analysis and integration of various datasets, such as road networks,
POI, and demographic data. GIS-based evaluations are commonly employed to assess street accessibility,
walkability, and the distribution of urban amenities. Research by Xiao et al. (2021) demonstrated how GIS-based
models, integrating POI and traffic data, can be used to assess the accessibility and pedestrian comfort of city
streets31. These approaches, coupled with demographic data, have allowed for a deeper understanding of how
street designs impact the accessibility and inclusivity of urban spaces. Similarly, Wang et al. (2022) applied GIS
to assess the impact of green spaces on urban street quality, finding that areas with higher green coverage tend
to exhibit better pedestrian experiences and overall street satisfaction32.
Furthermore, the integration of 3D modeling and virtual reality (VR) technologies into street quality research
has provided new possibilities for spatial analysis. In recent years, 3D modeling techniques have gained popularity
for their ability to represent urban streets in high detail. 3D models, particularly those generated using virtual
reality (VR) and augmented reality (AR) technologies, allow for immersive and interactive experiences that aid
in evaluating street environments. Studies like those by Zhao et al. (2022) have explored how 3D simulations
can be used to assess not only the visual appeal of streets but also their functionality in terms of pedestrian
movement, traffic flow, and environmental conditions33. This method offers a more comprehensive approach to
street evaluation, incorporating both physical and experiential aspects of street quality. Furthermore, Liu and
Wang (2023) developed a 3D GIS model that enables real-time evaluation of urban streets, incorporating traffic
data, pedestrian flow, and environmental attributes to create a holistic street quality assessment framework34.
While these advancements have enhanced the capabilities of street quality research, there remain challenges
related to the vast amounts of data involved and the complexity of processing such data. Large-scale refinement
of urban street evaluations, using diverse data types such as POI, heat maps, GIS layers, and 3D models, presents
significant difficulties in data integration and analysis. The variability of data formats, inconsistencies in data
quality, and the need for advanced computational tools to process and synthesize these complex datasets continue
to pose obstacles. Nonetheless, the combination of big data and advanced spatial analysis techniques holds
great potential for revolutionizing the study of urban street environments. Recent studies have also emphasized
the importance of machine learning (ML) techniques to overcome these challenges. For example, Wang et al.
(2023) employed deep learning algorithms to automatically classify and analyze street images and POI data,
significantly improving the efficiency and accuracy of street quality assessments35. Such approaches represent
the next frontier in urban research, where automation and advanced analytics play a key role in handling the
complexity of big data in urban planning.
Street quality research based on big data and artificial intelligence
In recent years, the rapid development of big data technologies and artificial intelligence (AI) has significantly
transformed the field of urban street quality research. Traditionally, street quality assessment relied on manual
evaluations and qualitative metrics. However, with the advent of big data and machine learning (ML), the
scope of analysis has expanded dramatically, allowing for more efficient, scalable, and objective evaluations of
urban streets. Among the most promising techniques are deep learning algorithms, particularly convolutional
neural networks (CNNs), which have demonstrated substantial success in image analysis and spatial pattern
recognition.
Machine learning, a concept introduced by Samuel in 1959, has paved the way for intelligent systems that
learn from data and improve over time36. Deep learning, a subfield of ML, has taken this further by enabling
computers to process and interpret vast amounts of visual and behavioral data. Algorithms such as Fully
Convolutional Networks (FCNs), ResNet and SegNet now allow for sophisticated analysis of images and spatial
data. These models can extract visual features from street-level imagery, such as roads, buildings, sidewalks, trees,
and green spaces, enabling researchers to assess street quality in a manner that was previously impossible37,38.
The application of deep learning to urban research is particularly evident in the analysis of streetscape
imagery. Through deep learning techniques, researchers are now able to automatically identify and classify
various urban elements, which can then be used to quantify street quality and inform urban design decisions.
A notable project, the “Place Pulse” initiative, launched by MIT’s Media Lab, collected public evaluations of
cityscapes through online surveys and paired photos. This project provided a large dataset (over 1.17 million
image pairs) that has become a valuable resource for understanding public perceptions of urban environments39.
By analyzing this data, researchers can examine how different visual elements of streetscapes (e.g., the presence
of greenery, building heights, and overall design) contribute to perceptions of aesthetic appeal and urban quality.
Zhang (2020) utilized deep learning methods and the Place Pulse dataset to evaluate urban street quality
in Beijing and Shanghai. By correlating visual elements with public perception scores, the study identified key
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 3

www.nature.com/scientificreports/
features that influence perceptions of street environments. The results highlighted the significant role of visual
factors such as trees, greenery, and the built environment in shaping perceptions of street quality and urban
livability. Additionally, the study considered multiple dimensions, including beautiful, wealthy, safety, lively,
depressing, and boring, which all play a crucial role in shaping the overall perception of street environments40.
Other studies, such as those by Liu et al. (2021) and Li and Guo (2021), have followed similar approaches,
expanding the use of deep learning to other urban quality indicators like safety, walkability, and environmental
comfort41,42.
In addition to visual perception analysis, AI and big data are increasingly being used to predict various factors
that influence street quality. In 2021, Wang et al. applied deep learning models to predict street walkability
in Beijing, incorporating factors such as street view images, traffic patterns, and environmental data43. Their
work demonstrated the ability of AI to assess how street design and environmental factors impact pedestrian
comfort and overall street vitality. This predictive capability allows urban planners to identify areas in need of
improvement and to make data-driven decisions regarding urban infrastructure.
The integration of big data and artificial intelligence in street quality research is highly relevant to current
trends in urban studies, urban planning, and smart city development. As cities continue to grow and face
increasingly complex challenges related to sustainability, mobility, and livability, AI and big data offer critical
tools for understanding and improving urban spaces. The ability to quantify street quality, predict environmental
changes, and optimize urban design based on data-driven insights is central to the development of more resilient
and adaptable cities. Moreover, the insights derived from AI-driven analysis can inform policy-making and
urban planning strategies, promoting the creation of more sustainable, inclusive, and livable urban environments.
As the field progresses, there is an increasing emphasis on using AI and big data to create “smart cities” where
real-time data is collected and analyzed to optimize urban living. This research trend aligns with the global
push towards data-driven decision-making in urban development, marking a paradigm shift in how cities are
planned, designed, and experienced.
Materials and methods
Study area
This research focuses on Jinan (Fig. 1), the capital of Shandong Province, covering 7,200 square kilometers with a
population of approximately 9 million. As a key political, economic, cultural, and transportation center, Jinan has
seen significant urban development in recent years, the municipal government has implemented various policies
and programs aimed at improving street infrastructure, environmental functions, and the urban landscape.
Notably, these initiatives include road network upgrades, the expansion of green spaces, the introduction of
smart city technologies for traffic management, and efforts to enhance pedestrian-friendly environments. These
policies have significantly contributed to the improvement of street quality and the overall urban landscape.
Jinan was selected for this study due to its recent urban improvements and availability of high-quality street
image data, which enhances the accuracy of street quality assessments. While other Chinese cities also have
ample street image data, Jinan stands out due to its comprehensive urban development initiatives, making it a
representative case for studying street quality in rapidly urbanizing cities.
Fig. 1. Study area.
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 4

www.nature.com/scientificreports/
Research framework
The study proposes a large-scale quantitative assessment method for street spatial visual perception (Fig. 2) to
explore the intrinsic connection between different street components and human perception and to further
supplement the results of spatial perception of streets with spatial syntax. The research framework consists of
three main processes: (1) Using the free and open API interface of Baidu Maps to obtain street view images, and
constructing the street view image dataset in the study area. (2) The elemental composition of urban streets is
extracted using the SegNet semantic segmentation model, and the human-computer confrontation model is
used to quantitatively analyze the spatial visual perception of streets, and the spatial syntax is used to process the
urban street network, and the accessibility of each street is measured on the basis of the 500 m accessibility radius
(the average walking distance of residents). (3) The results of street accessibility analysis and visual perception
scores are superimposed and analyzed to establish an evaluation matrix based on the dimensions of “quality
evaluation” and “accessibility” to find out “streets with potential for renewal” in the study area. The results are
used to identify “streets with renewal potential” in the study area, and to provide refined technical support for
urban micro-renewal.
Constructing street view image dataset
In recent years, street view data has been widely used in urban planning studies44, and street view images
present information about urban infrastructure from a pedestrian perspective45. Street view platforms provide
APIs that allow users to batch download street view data and provide street view browsing services. In order to
comprehensively measure the visual perception evaluation of street space by residents in the study area, the study
set up street view data collection points at 50 m intervals. Throughout the study area, 57,527 Street View collection
points were generated within the OSM street network. A total of 30, 511 street view images were collected using
Python and the Baidu Street View Map API (https://api.map.Baidu.com/panorama/v2?ak=YOURKEY).
In order to accurately simulate the residents’ perception, the specific parameters for retrieving Baidu street
view images from the API were set as follows: the vertical angle (pitch) was set to 20° and the field of view width
(fov) was set to 90°. For each sampling point, a 360° panoramic view of the street was obtained by stitching the
views in four directions. An example of the downloaded street view image is shown in (Fig. 3).
Deep learning based semantic segmentation of street view images
This study uses an improved semantic segmentation model based on the encoder-decoder structure SegNet, an
open-source deep convolutional neural network released in 2015 by researchers at the University of Cambridge.
Fig. 2. Research framework.
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 5

www.nature.com/scientificreports/
Fig. 3. Example of the BSVIs collection process.
SegNet model is due to its demonstrated efficiency and accuracy in processing high-resolution images, and its
structural flexibility allows it to effectively adapt to the complex backgrounds and diverse elements found in
urban visual analysis. Compared to other potential models such as U-Net and Fully Convolutional Networks
(FCN), SegNet has significant advantages in maintaining spatial information and detail recovery, which are
crucial for accurately identifying various visual elements in street scenes46. The encoder part of SegNet consists
of multiple convolutional and pooling layers, which progressively reduce the size of the feature map and extract
abstract features. The decoder part, on the other hand, consists of an upsampling layer and a convolutional layer,
which are used to map the features extracted by the encoder back to the size of the original image and generate
pixel-level classification results47. The semantic segmentation model used in this study was trained and tested
on the ADE 20 K dataset, achieving 82.538% pixel accuracy on the training dataset and 68.432% pixel accuracy
on the test dataset.
The backbone encoder network in the model is ResNet50, which consists of a convolution (conv) module
and an identity module. The conv module has different input and output dimensions and cannot be placed
in series, whereas the identity module has the same input and output dimensions as the other modules and
can be used in series. The structure of the network model is shown in Table 1. The neural network is divided
into four parts: input, encoding, decoding, and output. The input layer reshapes any pixel image to a size of
416 × 416, with the input image elements having three dimensions: R, G, and B. Conv2D is used to construct a
convolutional layer to extract features from the input high-dimensional array. The batch normalization method
proposed by Ioffe and Szegedy in 2015 is used to improve the training speed and generalization ability of the
network48. MaxPooling2D is used to reduce the image dimensions and neuron parameters without sacrificing
image features. UpSampling2D is used to restore the original image size. The encoder resizes the image to a size
of 43,264 (208 × 208). Softmax calculates the probability of a particular semantic classification for each pixel
across 150 categories.
The ADE 20 K dataset (Fig. 4) was used as the training dataset because the images contain 150 objects from
everyday life, such as the sky, roads, cars, and plants. Each image is labeled with pixel-level scene segmentation
labels to indicate different objects and regions in the image. Using this dataset to train the model significantly
improves the experimental accuracy.
Perceptual scoring of street view images using a Human- machine adversarial scoring framework
This study refers to the human-machine adversarial scoring framework proposed by Yao to predict visual
perception scores49, which is able to more comprehensively assess the quality of different dimensions of visual
perception in cities by combining the results of subjective human scoring and automatic machine scoring. Two-
thirds of the sample data in the scoring model were randomly selected for model fitting, while the remaining
one-third was used as test data to assess the accuracy of the overall model.
The Place Pulse project at the MIT Media Lab rated street images in six emotional perceptions: beautiful,
wealthy, safe, lively, depressing, and boring50,51, which are six dimensions that provide a comprehensive picture
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 6

www.nature.com/scientificreports/
Framework Layer type Output shape Neuronal parameters
Input Input layer (None, 416, 416, 3) 0
Conv2D (None, 208, 208, 64) 9472
Batch normalization (None, 208, 208, 64) 256
Activation (None, 208, 208, 64) 0
Encoder
MaxPooling2D (None, 103, 103, 64) 0
……
ZeroPadding2D (None, 28, 28, 1024) 0
Conv2D (None, 26, 26, 512) 4,719,104
Batch normalization (None, 26, 26, 512) 2048
UpSampling2D (None, 52, 52, 512) 0
Decoder
ZeroPadding2D (None, 54, 54, 512) 0
……
Batch normalization (None, 208, 208, 64) 256
Output Softmax (None, 43,264, 150) 0
Total parameters: 14,947,414
Table 1. Structure of the neural network architecture.
Fig. 4. ADE20K dataset (ADE20K dataset (mit.edu)).
of the quality of visual perception of streets from the residents’ perspective. Additionally, based on these six
urban street perception dimensions, an increasing number of scholars have conducted extensive studies related
to human perception of cities52,53. A high or low score for each dimension represents the degree of perceptual
recognition by residents, with higher scores indicating stronger perceptions of the dimension. We further
categorized these six dimensions into positive and negative spatial perceptions to assess the quality of urban
streets from the residents’ perspective. Therefore, the six perception types mentioned above were utilized to
explore the quality of visual perception of urban streets with a people-oriented approach. In order to more
accurately determine the perception of street quality in the study area, 128 volunteers were recruited to conduct
the urban perception assessment.
The schematic diagram of using the human-computer adversarial model to assess the quality of urban streets
is shown in (Fig. 5). The volunteers first used the human-machine adversarial model to rate the six dimensions
of beauty, boredom, depression, liveliness, affluence, and safety on a scale ranging from 0 to 6, with higher scores
representing greater congruence with the rated dimensions. This scale was chosen because it provides a balance
between perceptual differentiation and ease of understanding for the volunteers. Although some studies such
as Wang et al.(2022) used a scale from 1 to 100, the choice of a 0–6 range was deemed more appropriate for this
context which focus on the primary emotional perceptions rather than highly granular distinctions, it facilitates
broader categorization while minimizing cognitive load for participants54.
During the implementation of the human-machine adversarial scoring framework and volunteer assessments,
several potential biases could arise. Firstly, volunteer subjectivity and inconsistent scoring standards may lead
to variability in the scoring results, reducing the reliability of the assessments. Volunteers might have different
interpretations of the rating scales or personal preferences that influence their evaluations. Secondly, the Random
Forest model, while robust, may encounter challenges such as overfitting, especially if the training data lacks
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 7

www.nature.com/scientificreports/
Fig. 5. Overview of the spatial perception scoring process for urban streets based on a machine learning.
sufficient diversity, which can impair its ability to generalize to new, unseen data. Additionally, the model might
misclassify complex or ambiguous street view images, affecting the overall accuracy of the visual quality scores.
To address potential biases, we implemented the following strategies: Comprehensive Training and
Standardization—Volunteers underwent extensive training sessions where clear guidelines and standardized
scoring criteria were provided. This aimed to harmonize the understanding and application of the rating scales,
thereby minimizing individual subjective differences. We utilized cross-validation to evaluate the model’s
performance across different subsets of data, ensuring that the Random Forest model maintained high accuracy
and stability. Additionally, feature importance analysis was conducted to identify and prioritize the most
influential visual elements, enhancing the model’s interpretability and robustness.
Each volunteer was asked to subjectively rate the first 1,000 street view images for each dimension, after
which the model constructed a random forest dataset. Random Forest, as an ensemble learning method,
effectively handles high-dimensional data and captures complex nonlinear relationships between variables by
constructing multiple decision trees and combining their prediction results. In this study, Random Forest was
utilized to analyze the relationship between volunteer scores and the extracted visual elements in the street
view images, thereby predicting visual quality scores for unscored images. Specifically, the model first used the
volunteer-scored data as the training set to learn the influence of different visual elements (such as sky, buildings,
plants, etc.) on the scores for each perception dimension. Then, the trained Random Forest model was applied to
predict the scores for the test set, and its performance and stability were evaluated through cross-validation and
feature importance analysis. This process not only enhanced the accuracy of score predictions but also improved
the model’s generalizability across different urban environments, enabling reliable visual quality assessments
in a broader range of application scenarios. The selection of 1,000 images was based on considerations of time
constraints, volunteer fatigue, and ensuring sufficient variability in the visual elements. Starting with 1,001 street
view images, the model recommended scores for the specified dimensions based on the relationship between the
volunteer’s previous scores and the visual elements in the street view images.
Street accessibility analysis and combined street quality portfolio analysis
Spatial syntax allows complex street designs to be represented as a mathematical graph containing various nodes
in order to study the characteristics of their spatial structure55, and is also commonly used in the analysis of
urban spaces with axial and segmental models56. Although axial models have been used in previous studies,
they have limitations in performing studies with large-scale urban applications57. In particular, these models
do not consider the scale of urban space58, modeling data cannot be obtained directly from existing urban data,
and the modeling time cost is large, making it difficult to cope with large spatial scales of research. In addition,
this study aims to study the accessibility of urban residents during their daily trips, so it is necessary to consider
the daily walking distance of urban residents as the accessibility radius, which is not supported by the axial
model. Therefore, this study uses a segmentation model based on the axial model to measure the accessibility
of urban streets. The segmentation model provides three modes to comprehensively analyze the topological
geometry, angles and distances of the street network. The difference between these analysis modes is the different
mathematical definitions of the shortest path. In the angular mode of the line segment model, the shortest path
is the path with the smallest combined turning angle between two line segments, which is one of the most
commonly used analytical modes in the line segment model. In his study, Hillier concluded that there is a high
correlation between the deflection angle of a roadway network and pedestrian trips, and the angular mode is
more in line with people’s perceptions under natural trips than the other models59. Residents do not have a God-
like perspective of urban space and therefore do not deliberately choose routes that are closer together. Instead,
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 8

www.nature.com/scientificreports/
streets with small turning angles are perceived as long and straight, tend to have a stronger sense of direction,
may be visually closer, wider in scale, and are habitually more likely to be selected60. In contrast, Ye explored the
accessibility of urban streets in Singapore using the angular pattern of segmental modeling in order to determine
the distribution of greenscapes in space from a human-centered perspective61.
Based on the advantages of this model, this study utilizes it to assess the accessibility of urban streets. OSM
line data was used as the raw data for spatial syntax, and GIS tools were employed to apply buffering to the roads.
The centerline was then extracted from the buffer to construct a new road network. Finally, street merging, street
simplification, and topology processing were performed on the road network to ensure accurate accessibility
calculation. According to the accessibility formula (Eq. 1) proposed by Hillier & Hanson we calculated the
accessibility value for each space62.
Equation (1) is as follows:
C i = n p − 1 n q d p d d p ( d i) (1)
∑ ∑
C iis the reachability value of space i, d pd refers to the shortest path from space p to space q. d pd(i) denotes the
shortest path between spaces p and q containing space i(p < q, p = 1, 2, 3…, n − 1, q = 2,3, 4…, n).
The study uses depthmapX to visualize street accessibility and applies it to the calculation of various urban
street scales. Using the daily walking distance of residents as the reachability radius, a review of related studies
found that the average daily walking distance of residents in first- and second-tier cities in China is about 500 m63.
Therefore, we set 500 m as the reachability radius and calculated the reachability of each street accordingly.
The street quality score was obtained by adding the scores of positive street perception and subtracting
the negative perception score, and the street space was comprehensively evaluated by combining with the
street accessibility analysis, and finally the street renewal measures were proposed by analyzing the quality
characteristics of the streets under different levels of evaluation.
Analysis of results
Analysis of street view image components
The study utilizes a deep learning model for semantic segmentation of street view images to identify and
categorize various street visual elements at each street data point. For each element type, the proportion within
a street image is calculated as the mean value across all sampled images. The top eight elements by proportion
are defined as follows:
• Sky: The area of the image depicting the sky, including both clear and cloudy conditions. This encompasses all
visible portions above the horizon line, excluding any obstructions such as buildings or trees.
• Building: All structures adjacent to the street, including residential, commercial, and industrial buildings. This
category includes facades, rooftops, and any architectural elements that are part of the built environment.
• Plant: Vegetation elements such as trees, shrubs, and landscaped greenery along the streetscape. This includes
street trees, planter boxes, green walls, and any other plant-based features that contribute to the urban green-
ery.
• Motorized road: Roadways designated for motor vehicle traffic, excluding pedestrian areas. This includes lanes
for cars, buses, trucks, and other motorized vehicles, as well as associated infrastructure like traffic signals and
signage.
• Vehicle: Motor vehicles present on the streets, including cars, buses, trucks, bicycles, and motorcycles. This
category captures both stationary and moving vehicles within the street view images.
• Wall: Walls used to control traffic flow or protect pedestrian safety, such as isolation walls at the edges of side-
walks, protective barriers in the center of roads.
• Sidewalk: Pedestrian pathways adjacent to the streets, designated for foot traffic. This includes sidewalks,
crosswalks, pedestrian islands, and any other infrastructure intended for pedestrian use.
• Person: Individuals walking along the streets, captured in the images. This includes single persons, groups,
and any visible human activity within the street view.
The spatial distribution of these elements is illustrated in Fig. 6, demonstrating their prevalence and
arrangement across different urban street areas. By clearly defining each visual element, this study ensures that
the categorization process is transparent and reproducible, facilitating consistent analysis and comparison across
different datasets and study areas.
Analysis of visual perception of streets based on BSVI
The human-computer adversarial model’s predicted scores for the six emotional dimensions of perception were
visualized in Arcgis using kriging linear interpolation (Fig. 7). The urban streets in Jinan received high scores
on beauty and liveliness owing to the well-designed greening efforts and orderly street layout. The wealthy
perception score reflects the fact that the economic development of Jinan urban area is centered on Lixia and
Shizhong districts, radiating to the surrounding high-tech district, Tianqiao district and other urban areas,
forming an interactive relationship between the geometric central area and the peripheral areas. Second. The
spatial distribution of street safety scores is somewhat similar to affluence scores, i.e., the level of economic
development has a direct impact on law and order and residents’ sense of security, and the more economically
developed, the better the law and order is in relative terms. Most of the places with high depressing perception
scores are located in old urban areas, where relatively narrow streets as well as dense building complexes cause
residents’ depressing perceptions to increase. Areas with high boring perception scores are mainly distributed
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 9

www.nature.com/scientificreports/
Fig. 6. Spatial distribution of streetscape constituent elements.
Fig. 7. Analysis of the six dimensions of emotional perception in the study area.
along the city’s main roads, indicating that they are built in a monolithic way, which may be related to the urban
function of the area. Instead of creating landscape features, customization and uniformity are pursued during
the planning and construction of major urban roads.
Multiple regression analysis of visual perception and visual elements
This study explored the impact of various components of urban streets (sky, Motorized Roads, vehicles, plants,
buildings, walls, sidewalks, and pedestrians) on different visual perception dimensions (beautiful, wealthy, safety,
lively, depressing, and boring) through multiple linear regression analysis. The regression analysis results are
shown in Table 2, where the asterisk next to the coefficient indicates its statistical significance level (***P < 0.001:
indicates significant results at a 99.9% confidence level, with extremely high statistical significance, **P < 0.01:
indicates that the result is significant at a 99% confidence level and highly significant, *P < 0.05: Indicates that the
result is significant at a 95% confidence level).
This study utilizes regression analysis to uncover the impact mechanisms of various components of urban
streets on different dimensions of visual perception, providing data-driven insights for urban planning and
street design. By optimizing greenery, adjusting wall designs, improving roads and sidewalks, and promoting
pedestrian activities, the visual quality of streets and residents’ life satisfaction can be effectively enhanced,
thereby fostering more human-centered and sustainable urban development.
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 10

www.nature.com/scientificreports/
Sky Motorized road vehicles Plant Buildings Walls Sidewalks Person
Beautiful 0.010 0.025** − 0.007** 0.282*** − 0.075** − 0.259*** − 0.086*** 0.055***
Lively − 0.298*** − 0.022*** 0.039** 0.120*** − 0.393*** − 0.164*** − 0.060*** 0.154***
Safety − 0.052*** 0.071*** 0.0012** 0.350*** − 0.020* − 0.179*** 0.106** 0.23**
Wealthy − 0.110*** 0.075*** 0.013*** 0.104*** 0.112** − 0.138*** 0.041*** 0.033**
Depressing − 0.139*** − 0.159*** 0.012** − 0.099*** 0.250** 0.169*** 0.012*** − 0.023***
Boring 0.288*** − 0.028** − 0.026* − 0.068*** 0.236*** 0.236*** 0.043*** − 0.044
Table 2. Results of the multivariate linear regression analysis for the visual elements and perception scores.
Beta coefficient *p < 0.05, **p < 0.01 ,***p < 0.001
• Optimize greenery design: Research results indicate that plant coverage has a significant positive impact on
perceptions of beauty, liveliness, and safety. Therefore, urban planners should prioritize increasing street
greenery, such as planting trees and installing green walls, to enhance the overall visual quality of streets and
residents’ satisfaction.
• Adjust wall design: Walls have a significant negative impact on multiple dimensions of visual perception, in-
cluding beauty, liveliness, safety, wealth, and boredom, indicating that wall designs may need optimization. It
is recommended to use more aesthetically pleasing and functional wall materials or reduce the use of walls to
minimize their negative impact on visual quality.
• Improve motorized roads and sidewalks: Good motorized road and sidewalk design positively influences mul-
tiple perception dimensions, including beauty, liveliness, safety, and wealth. Urban planning should focus
on maintaining motorized roads and expanding sidewalk designs to enhance street accessibility and visual
quality.
• Promote pedestrian activities: Pedestrian activity has a significant positive impact on perceptions of liveliness
and safety. By increasing recreational facilities on streets and establishing convenient pedestrian pathways,
pedestrian activities can be promoted, thereby enhancing the overall liveliness and safety of streets.
Overlay analysis of street accessibility and street quality
The accessibility of urban streets in Jinan city is presented based on the daily walking distance of residents of
500 m (Fig. 8), the range of 0 to 6 in the map indicates the level of road accessibility, with 0 representing the
lowest accessibility and 6 representing the highest accessibility. Most of the highly accessible streets are urban
arterials, which bear the main traffic flow of the city, connecting urban areas with important regions, with high
vehicle and pedestrian traffic, and are usually designed with multiple lanes. Secondly, compared with the central
and western regions, the distribution of highly accessible streets in the southeast region is relatively sparse. With
the advancement of urban development planning, urbanization in the Southeast region has accelerated, and
street accessibility has been improved by increasing the number of lanes, constructing pedestrian paths, and
strengthening transportation infrastructure. Overall, major transportation arteries basically cover the urban
area, with a well-developed transportation network and high connectivity within and outside the region, which
promotes economic development and facilitates the flow of people and goods.
Combining the measurement of street quality and the overlay analysis of street network accessibility, the aim
is to evaluate the current spatial status of streets using the “accessibility-quality” evaluation dimension, and to
discuss which streets have high quality and accessibility and good spatial quality of places, and which streets have
high pedestrian accessibility but unsatisfactory quality, indicating that although they have good potential for
pedestrian activities, they still need to be improved in terms of perceived quality. The evaluation of streets with
high accessibility and good spatial quality of place, and those with high walkability but poor quality, indicates
that although they have good potential for walking activities, they still need to be improved in terms of perceived
quality, thus identifying potential problems in improving the quality of the streets.
In this overlay analysis, the median value of road accessibility in the study area was used to categorize
accessibility into “high accessibility” and “low accessibility”, and the median value of street quality measures was
used to categorize spatial quality into “high quality” and “low quality”. The median value of the street quality
measurement results is used to categorize the spatial quality into “high quality” and “low quality”, and the two
dimensions can be integrated to divide the streets into four major categories: high quality/high accessibility;
high quality/low accessibility; low quality/high accessibility; low quality/low accessibility; and their distribution
is shown in Fig. 9.
High quality/accessibility: These streets score well in both environmental quality and pedestrian accessibility,
offering strong spatial potential. They are relatively few and primarily located in urban centers. High quality/
low accessibility: found mainly at district junctions, these streets feature high greening rates and well-developed
infrastructure, contributing to strong quality scores. However, their sparse surrounding road networks result
in low pedestrian accessibility. Low quality/high accessibility: these streets, often situated southwest of the city
center, benefit from good pedestrian accessibility but lack essential street furniture and greenery, leading to
lower quality scores. Low quality/low accessibility: these streets require particular attention in urban planning.
Predominantly located on the city’s periphery, they are characterized by aging buildings, low structures, and
fragmented street networks, which hinder accessibility. To enhance these areas, urban planning efforts should
prioritize functional improvements, building façade renovations, and increased greenery. Strengthening street
quality and vitality while gradually expanding the pedestrian network will be key to their transformation.
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 11

www.nature.com/scientificreports/
Fig. 8. Accessibility of the streets within a walking distance of 500 m for urban residents in the study area.
Conclusion
This study constructs a method for evaluating the visual perception of urban streets using spatial syntax theory
and artificial intelligence technology, with a human-centered approach. The evaluation of street quality and
micro-renewal potential is carried out through accessibility analysis and overlay analysis of urban streets.
Additionally, the study employs a visual perception score combined with multiple regression analysis to reveal
the influence mechanisms of street components on visual perception. The methodology applied in this study
provides an effective way to measure the spatial quality of urban streets, offering data-driven suggestions for
improving street quality. The analysis of spatial perception and visual elements can be applied to various stages
of urban street development and management, contributing valuable insights for future urban planning.
As an emerging technology in urban analysis, this approach has significant advantages in large-scale, human-
centered planning and design. First, in terms of data acquisition, using streetscape images to study the spatial
quality and vitality of urban spaces is more time- and cost-efficient than traditional methods such as manual
surveying or photography. Second, in terms of research methodology, using large-scale streetscape data for
quantitative analysis offers more reliable results than traditional qualitative research or small-scale audits. Third,
from a research perspective, combining objective streetscape data with residents’ subjective perceptions allows
for efficient and scientifically informed urban analysis, addressing urban issues in a problem-oriented manner.
This approach contributes to a more rational and data-driven process in urban planning and design.
Furthermore, the findings of this study have practical applications for policymakers and urban planners.
For instance, the identification of streets with high accessibility but low visual quality can inform targeted
interventions to enhance these areas. By implementing targeted greening measures, such as increasing street
tree density or adding green walls, policymakers can improve pedestrian safety and overall street aesthetics.
Additionally, the insights gained from the multiple regression analysis can help in designing micro-renewal
projects that address specific visual and functional deficiencies, thereby fostering more vibrant and sustainable
urban environments.
Despite the advantages of this approach, the study does have some limitations. Due to constraints in data
sources, the street view data was collected and photographed from the viewpoint of the roadway, which may
introduce discrepancies when compared with the actual pedestrian perspective, as much of the public space
used by people for daily activities is primarily located along walking paths. Additionally, limitations in the
machine learning algorithms and the resolution of the street view data meant that certain key elements, which
could impact spatial quality, were not included in this analysis. This resulted in some potential inaccuracies
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 12

www.nature.com/scientificreports/
Fig. 9. Quality/accessibility distribution map.
and limitations in the quality evaluation, we will incorporate advanced analysis algorithms to address these
shortcomings in the future research. Furthermore, the data from different times could be used to analysis the
trends in the spatial quality of urban streets over time. By analyzing urban street planning and development
from both spatial and temporal dimensions, we aim to predict future trends and improve the accuracy of urban
planning decisions. Future studies could also explore the integration of real-time data sources and temporal
street view images to capture dynamic changes in urban environments, thereby providing a more comprehensive
understanding of how visual perception evolves over time.
Data availability
The datasets used and/or analyzed during the current study are available from the corresponding author on
reasonable request.
Received: 24 September 2024; Accepted: 19 May 2025
References
1. Oc, T. & Tiesdell, S. Urban Design: Ornament and Decoration (Routledge, 2007).
2. Mehta, V. The Street: a Quintessential Social Public Space (Routledge, 2013).
3. Yin, L., Cheng, Q., Wang, Z. & Shao, Z. Big data’for pedestrian volume: exploring the use of google street view images for pedestrian
counts. Appl. Geogr. 63, 337–345 (2015).
4. Runge, N., Samsonov, P., Degraen, D. & Schöning, J. No more autobahn! Scenic route generation using Googles street view. In
Proceedings of the 21st International Conference on Intelligent User Interfaces, 147–151 (2016).
5. Hou, Y. et al. Global streetscapes—A comprehensive dataset of 10 million street-level images across 688 cities for urban science and
analytics. ISPRS J. Photogrammetry Remote Sens. 215, 216–238 (2024).
6. Zhang, F. & Yu, L. I. U. Street view imagery: methods and applications based on artificial intelligence. Natl. Remote Sens. Bull.
25(5), 1043–1054 (2021).
7. Kopf, J., Chen, B., Szeliski, R. & Cohen, M. Street slide: browsing street level imagery. ACM Trans. Graphics (TOG). 29(4), 1–8
(2010).
8. Hoelzl, I. & Marie, R. Google street view: navigating the operative image. Visual Stud. 29(3), 261–271 (2014).
9. Torii, A., Havlena, M. & Pajdla, T. From google street view to 3d city models. In 2009 IEEE 12th international conference on
computer vision workshops, ICCV Workshops, 2188–2195 (IEEE, 2009).
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 13

www.nature.com/scientificreports/
10. Anguelov, D. et al. Google street view: capturing the world at street level. Computer 43(6), 32–38 (2010).
11. Hara, K. et al. Improving public transit accessibility for blind riders by crowdsourcing bus stop landmark locations with Google
street view: an extended analysis. ACM Trans. Accessible Comput. (TACCESS). 6(2), 1–23 (2015).
12. Li, X., Zhang, C. & Li, W. Does the visibility of greenery increase perceived safety in urban areas? Evidence from the place pulse 1.0
dataset. ISPRS Int. J. Geo-Information. 4(3), 1166–1183 (2015).
13. Clews, C. et al. Alcohol in urban streetscapes: a comparison of the use of Google street view and on-street observation. BMC
Public. Health. 16, 1–8 (2016).
14. Oh, K. Visual threshold carrying capacity (VTCC) in urban landscape management: A case study of Seoul, Korea. Landsc. Urban
Plann. 39(4), 283–294 (1998).
15. Li, X. et al. Assessing street-level urban greenery using Google street view and a modified green view index. Urban Forestry Urban
Green. 14(3), 675–685 (2015).
16. Shen, Q. et al. StreetVizor: visual exploration of human-scale urban forms based on street views. IEEE Trans. Vis. Comput. Graph.
24(1), 1004–1013 (2017).
17. Jacobs, J. The death and life of great American cities. 21(1), 13–25 (1961).
18. Lefebvre, H. The production of space (1991). In The People, Place, and Space Reader, 289–293 (Routledge, 2014).
19. Lynch, K. The image of the environment. Image City. 11, 1–13 (1960).
20. Gehl, J. Cities for People. (2010). (2013).
21. Jacobs, A. & Appleyard, D. Toward an urban design manifesto. In The City Reader, 640–651 (Routledge, 2015).
22. Whyte, W. H. The social life of small urban spaces. (1980).
23. Hillier, W. R. G. & Shu, S. Crime and urban layout: the need for evidence. (1999).
24. Batty, M. Spatial analysis and urban form: integrating methods and techniques. J. Royal Stat. Society: Ser. (Statistics Society). 166(1),
5–22 (2003).
25. Carrión, D. & Bote, E. Street networks and accessibility: A comprehensive review of spatial syntax applications. J. Urban Plann.
16(4), 312–331 (2015).
26. Zhang, T. & Lee, M. Evaluating pedestrian walkability in urban streets: A GIS-based approach. Urban Des. Int. 21(3), 168–180
(2016).
27. Zhang, X., Wang, L. & Li, J. Combining POI data with public awareness tasks for street type identification. J. Urban Stud. 45(3),
215–230 (2019).
28. Liu, Y., Zhang, F. & Wang, Y. The influence of street design on commercial vitality: A POI-based analysis. Urban Plann. Rev. 34(2),
112–126 (2021).
29. Qin, Y., Zhang, R. & Liu, F. Quantitative evaluation of street vitality in tourist cities based on POI, Baidu heat map, and OSM road
network data. Urban Inf. 12(2), 108–119 (2020).
30. Zhao, X., Li, J. & Guo, L. Integrating weather and traffic data for street vitality analysis in tourist cities. Urban Stud. 58(8), 1463–
1480 (2021).
31. Xiao, D., Wang, X. & Huang, Z. GIS-based evaluation of street accessibility and pedestrian comfort: A case study. Urban Des. J.
36(4), 320–335 (2021).
32. Wang, X., Liu, J. & Huang, L. Assessing the impact of green spaces on urban street quality using GIS. J. Environ. Des. 42(1), 88–102
(2022).
33. Zhao, Q., Zhang, P. & Liu, X. Using 3D virtual reality technology for street quality assessment: A case study in urban China. City
Environ. 25(1), 98–112 (2022).
34. Liu, Q. & Wang, S. Real-time 3D GIS model for street quality assessment: A case study of Beijing. Geospatial Inform. Sci. 38(5),
198–212 (2023).
35. Wang, H., Li, J. & Guo, Q. Deep learning for street image and POI data classification: enhancing urban street evaluation. J.
Geospatial Res. 48(5), 345–360 (2023).
36. Samuel, A. L. Some studies in machine learning using the game of checkers. IBM J. Res. Dev. 3(3), 210–229 (1959).
37. Long, J., Shelhamer, E. & Darrell, T. Fully convolutional networks for semantic segmentation. In Proceedings of the IEEE Conference
on Computer Vision and Pattern Recognition (CVPR), 3431–3440. (2015).
38. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition (CVPR), 770–778. (2016).
39. Zhang, H. Understanding Human Perceptions of Street View Images Using MIT Place Pulse 2.0 Dataset (Doctoral dissertation,
Waseda University). (2023).
40. Zhang, T. Evaluating urban street quality using deep learning and place pulse dataset: A case study of Beijing and Shanghai. Urban
Stud. J. 57(5), 1013–1030 (2020).
41. Liu, H. & Wang, J. Deep learning for urban image analysis: A study of streetscape perceptions in new York City. J. Urban Technol.
28(4), 17–33 (2021).
42. Li, X. & Guo, Y. Street view image analysis using deep learning: Understanding factors affecting urban quality perceptions. Landsc.
Urban Plann. 204, 103980 (2021).
43. Wang, Z., Chen, X. & Zhao, L. Predicting street walkability using AI and deep learning: A case study of Beijing. Transp. Res. Part.
D: Transp. Environ. 88, 102616 (2021).
44. Cheng, L. et al. Use of tencent street view imagery for visual perception of streets. ISPRS Int. J. Geo-Information. 6(9), 265 (2017).
45. Rzotkiewicz, A., Pearson, A. L., Dougherty, B. V., Shortridge, A. & Wilson, N. Systematic review of the use of Google street view in
health research: major themes, strengths, weaknesses and possibilities for future research. Health Place. 52, 240–246 (2018).
46. Badrinarayanan, V., Kendall, A. & Cipolla, R. Segnet: A deep convolutional encoder-decoder architecture for image segmentation.
IEEE Trans. Pattern Anal. Mach. Intell. 39(12), 2481–2495 (2017).
47. Kolhar, S. & Jagtap, J. Convolutional neural network based encoder-decoder architectures for semantic segmentation of plants.
Ecol. Inf. 64, 101373 (2021).
48. Ioffe, S. Batch normalization: Accelerating deep network training by reducing internal covariate shift. arXiv preprint
arXiv:1502.03167. (2015).
49. Yao, Y. et al. A human-machine adversarial scoring framework for urban perception assessment using street-view images. Int. J.
Geogr. Inf. Sci. 33(12), 2363–2384 (2019).
50. Dubey, A., Naik, N., Parikh, D., Raskar, R. & Hidalgo, C. A. Deep learning the city: Quantifying urban perception at a global scale.
In Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part
I 14, 196–212 (Springer International Publishing, 2016).
51. Lou, A., Stancato, S. & Piga, B. E. G. Assessing in-motion urban visual perception: analyzing urban features, design qualities, and
people’s perception. In Advances in Representation: New AI-and XR-Driven Transdisciplinarity, 691–706 (2024).
52. Zhang, F. et al. Uncovering inconspicuous places using social media check-ins and street view images. Comput. Environ. Urban
Syst. 81, 101478 (2020).
53. Yang, J., Zhou, L. & Chen, W. Spatial patterns and multi-dimensional impact analysis of urban street. MDPI Electron. 13(21), 11740
(2023).
54. Wang, L., Han, X., He, J. & Jung, T. Measuring residents’ perceptions of city streets to inform better street planning through deep
learning and space syntax. ISPRS J. Photogrammetry Remote Sens. 190, 215–230 (2022).
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 14

www.nature.com/scientificreports/
55. Dawes, M. J., Ostwald, M. J. & Lee, J. H. Examining control, centrality and flexibility in Palladio’s villa plans using space syntax
measurements. Front. Architectural Res. 10(3), 467–482 (2021).
56. Atakara, C. & Allahmoradi, M. Investigating the urban spatial growth by using space syntax and GIS—A case study of famagusta
City. ISPRS Int. J. Geo-Information. 10(10), 638 (2021).
57. Hillier, B. & Iida, S. Network and psychological effects in urban movement. In International Conference on Spatial Information
Theory, 475–490 (Springer, 2005).
58. Pafka, E., Dovey, K. & Aschwanden, G. D. Limits of space syntax for urban design: axiality, scale and sinuosity. Environ. Plann. B:
Urban Analytics City Sci. 47(3), 508–522 (2020).
59. Lerman, Y., Rofè, Y. & Omer, I. Using space syntax to model pedestrian movement in urban transportation planning. Geographical
Anal. 46(4), 392–410 (2014).
60. van Nes, A., Yamu, C., van Nes, A. & Yamu, C. Analysing linear spatial relationships: the measures of connectivity, integration, and
choice. Introduction to Space Syntax in Urban Studies, 35–86 (2021).
61. Ye, Y. et al. Measuring daily accessed street greenery: A human-scale approach for informing better urban planning practices.
Landsc. Urban Plann. 191, 103434 (2019).
62. Hillier, B. & Hanson, J. The Social Logic of Space (Cambridge University Press, 1984).
63. Lyu, Y. & Forsyth, A. Attitudes, perceptions, and walking behavior in a Chinese City. J. Transp. Health. 21, 101047 (2021).
Author contributions
Mingyang Yu and Xin Chen wrote the main manuscript text together. All authors reviewed the manuscript.
Funding
This work was supported by the National Natural Science Foundation of China, grant number (No. 41801308).
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to M.Y.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have
permission under this licence to share adapted material derived from this article or parts of it. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p: / / c r e a t i ve c o m m o
n s . or g / l i c e n s es / b y - n c - n d / 4 . 0 / .
© The Author(s) 2025
Scientific Reports | (2025) 15:18439 | https://doi.org/10.1038/s41598-025-03189-z 15
