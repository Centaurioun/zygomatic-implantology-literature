---
title: "Evaluation of Prostheses Retained Zygomatic and Dental Implants in Large Defects in the Maxilla Due to Tumors or Major Trauma by Biomechanical 3- Dimensional Finite Element Analysis"
authors:
  - "Hatice Yemeno\u011flu"
  - "Melek Beder"
  - "Murat Yaylac\u0131"
  - "Ayberk Dizdar"
  - "Murat Alkurt"
  - "Muhammed Enes Naralan"
  - "Ecren Uzun Yaylac\u0131"
  - "Mehmet Emin \u00d6zdemir"
  - "\u015eevval \u00d6zt\u00fcrk"
  - "Zeynep Ye\u015fil"
journal: "BMC Oral Health"
year: 2025
volume: "25"
issue: "1"
pages: "99-109"
doi: "10.1186/s12903-025-05468-7"
url: "https://bmcoralhealth.biomedcentral.com/articles/10.1186/s12903-025-05468-7"
source_file: "yemenoglu-2025-evaluation-of-prostheses-retained-zygomatic-and-dental-implants-in-large-defects.md"
---
# Evaluation of prostheses retained zygomatic and dental implants in large defects in the maxilla due to tumors or major trauma by biomechanical 3- dimensional finite element analysis

Hatice Yemenoglu1 , Melek Beder $1 , 8 ^ { * } \textcircled { \mathbb { D } } ,$ Murat Yaylacı2,3 , Ayberk Dizdar4 , Murat Alkurt5 , Muhammed Enes Naralan6 , Ecren Uzun Yaylacı7 , Mehmet Emin Özdemir9 , Şevval Öztürk2 and Zeynep Yeşi $\lvert 5 , 1 0 _ { \oplus }$

# Abstract

Background Zygomatic implants are becoming an ideal treatment approach for implant-supported prosthesis treatment developed for the atrophic maxilla. This study aims to evaluate the amount and distribution of stress in implants and peri-implant bone using different implant-supported prosthesis configurations in Aramany Class I maxillary defects through 3-dimensional finite element analysis.

Methods A 3-dimensional finite element model of the Aramany class I defect was created. Three different implantsupported prostheses were modelled: model 1: 1 zygomatic implant and 3 dental implants, model 2: 1 zygomatic implant and 2 dental implants, and model 3: 2 zygomatic implants. Vertical and horizontal loads of 150 N were applied in 6 different ways to the defected and non-defective areas. Maximum principal stress and von mises stresses in the bone surrounding the implants were evaluated.

Results When all loading conditions were evaluated with both porcelain layer on Co-Cr framework and acrylic layer on acrylic framework, the highest maximum principal stress value was observed in Model 3. In contrast, the lowest value was observed in Model 1. The highest maximum principal stress occurred when a horizontal load was applied simultaneously to both the defective and non-defective areas. In contrast, the lowest value was observed when a vertical load was applied to the non-defective area. The von Mises stress values were found to be similar across all models when both restoration materials were used.

Conclusions Based on the results of this study, it can be concluded that increasing the number of implants in the non-defective area reduces the highest stress value while using acrylic as a restoration material slightly increases the stress value.

Keywords Dental implant, Zygomatic implant, Finite element analysis

# Background

Maxillary defects resulting from causes such as tumours and trauma are commonly encountered in clinical practice [1]. After a maxillectomy, part of the maxilla is lost, creating a connection between the oral cavity, maxillary sinus, and nasal cavity [2]. As a result, the deterioration in chewing and speech negatively impacts the quality of life of patients [3]. Rehabilitation of atrophic maxillae with dental implants is challenging due to several limitations, including pneumatization of the maxillary sinus, severe alveolar bone resorption, and insufficient subnasal bone volume [4]. Various techniques have been proposed for the treatment of maxillary atrophy, including reconstruction of the maxilla with the iliac crest, elevation of the maxillary sinus floor, bone grafts, and titanium mesh. Some of these treatment options necessitate multiple surgical interventions. Additionally, these procedures have varying success rates and often involve high surgical costs. The application of zygomatic implants is a less invasive method that offers more predictable results [5]. Therefore, zygomatic implants, applied in various numbers and configurations, have been successfully used as a viable alternative to more complex surgical procedures in the rehabilitation of atrophic maxilla [6, 7].

Schmidt et al. [8], reported that the combination of zygomatic and standard endosseous implants can provide retention and support for maxillary obturator prostheses following extensive resection of the maxilla. As a result of the predictable implant support and retention provided, the planning of implant-supported obturator prostheses has become an effective treatment method [8–10]. However, the design of the dental superstructure significantly affects the loading of dental implants and bone deformation. This deformation can lead to excessive stress accumulation in the bone surrounding the implants, resulting in bone resorption and potential implant failure [11].

The transfer of load and distribution of stress in the implant-bone connection area are critical factors affecting the success rate of implants. Direct clinical evaluation is necessary to assess the biomechanical response of an implant to the surrounding bone. However, this is often impractical due to complex structures, lengthy operating times, and ethical concerns. Consequently, in vitro methods such as strain gauges, analytical techniques, experimental approaches, computational models, and finite element analysis (FEA) have been employed to evaluate the biomechanical behaviour of dental implants. Each of these methods has its advantages and limitations. However, FEA is indispensable for analysing situations involving numerous complex geometries and various implant configurations [3]. FEA is an effective computational tool adapted from the engineering field for dental implant biomechanics, allowing for the evaluation of stress [12]. FEA divides a complex body into smaller components that can be modelled separately using mathematical equations [13]. FEA is widely used to assess the biomechanical performance of various dental implant designs and their effects on clinical factors related to implant success [2]. With FEA, both the stress distribution on implants and abutments and the stress distribution in the bone supporting these implants can be evaluated [12].

This study aimed to evaluate the amount and distribution of stress in implants and peri-implant bone in prosthetic models designed with different configurations of zygomatic and dental implants for Aramany Class I maxillary defects. Additionally, the study aimed to understand the prognosis of these treatment options using FEA.

# Methods

FEA decomposes a model with continuous geometry into numerically simplified, smaller finite elements to address complex mechanical and physical problems in engineering applications [14, 15]. Apart from various technical fields, FEA is widely used in biomechanics [16–21] particularly in dental implantology and dental traumatology, as well as in general dentistry [22–24]. In the dental context, FEA can be applied in biomechanical analysis, stress analysis, and personalized treatment planning, which enhances its significance in the field of dental implantology.

In this study, the ANSYS Workbench software package (ANSYS 16.0, Swanson Analysis Systems Inc., Houston PA, USA) was utilized for numerical modelling and finite element analysis of the physical problem. To conduct a finite element analysis of an existing dental issue, an accurate numerical model must first be created. During this stage, the most appropriate geometry for the numerical model is developed, and the most suitable finite elements are selected to form the mesh structure. Choosing the right finite element geometry and size is crucial for the accuracy of the results. The mesh structure is constructed using the selected finite elements (geometry and mesh structure). The material properties for the created mesh structure are then defined (material properties). Finally, finite element analysis is performed based on the specified boundary conditions and loading scenarios (loads and boundary conditions).

# Geometry

In this study, cone beam computed tomography (CBCT) images were used to create the geometric contours of the finite element (FE) model for the diagnosis and treatment planning of a middle-aged woman with maxillary edentulism. In this context, the institutional approvals from the Faculty Board of Recep Tayyip Erdoğan University and the Non-Invasive Ethics Committee were obtained first. CBCT images of materials were acquired using the
Fig. 1 Creation of a 3D finite element model

NewTom VGI evo [Quantitative Radiology, Verona, Italy] with the following parameters: $1 2 5 ~ { \mu \mathrm { m } }$ voxel size, 110 Kvp, $4 . 0 6 ~ \mathrm { { m A } }$ , and a 6-second scan. CBCT images of a middle-aged woman with maxillary edentulism were randomly selected from the dentomaxillofacial radiology department archives and acquired using the NewTom VGI evo with the following parameters: $2 0 0 ~ { \mu \mathrm { m } }$ voxel size, 110 Kvp, 3 mA, and a 1.8-second scan.

Data consisting of radiographic images saved as Digital Imaging and Communications in Medicine (DICOM) files were imported into Mimics Innovation Suite 24.0 (Materialise NV, Leuven, Belgium) for segmentation. The bone structure, soft tissues, and teeth of the maxilla were separated by the original images. At this stage, while creating the solid model of the maxilla, each detail was segmented and refined according to image intensity using Materialize 3-matic 16.0 (Materialise, Belgium, Leuven). The 3D model of the maxillary structure was segmented and cleaned to match the original. After making the necessary adjustments to the 3D model using SolidWorks (Solidworks 2018, Dassault Systemes Solidworks Corporation. Waltham MA, USA.), a complete 3D reconstruction of the maxillary structure was created and integrated into the ANSYS Workbench program for finite element analysis (Fig. 1).

In this study, a standard dental implant (Nobel Biocare AB) with a diameter of $4 . 3 \ \mathrm { m m }$ and a length of $1 0 \ \mathrm { m m }$ and a height of $3 . 5 \ \mathrm { m m }$ multi-unit $( 0 ^ { 0 } )$ abutments, and a zygomatic implant (NobelZygoma $4 5 ^ { 0 }$ TiUnit, Nobel Biocare AB, Gothenburg, Sweden) with a diameter of $4 . 1 \ \mathrm { m m }$ and a length of $4 0 \ \mathrm { m m }$ and a height of $3 \ \mathrm { m m }$ multi-unit $( 0 ^ { 0 } )$ abutments were used. Titanium screws produced as standard for the implant used as screws were used. After the implants were modeled, they were mounted in their planned locations on the modeled skull. It was also assumed that implants were fully osseointegrated (in full contact).

Within the context of the study, modelling and analysis were conducted on three different scenarios for both the intact and defect regions of the maxilla. Zygomatic implant number 4 and standard dental implants numbered 2, 4, and 6 were projected into the maxilla in three different configurations (Fig.  2A, B, C). Finite element analyses were performed under various loading conditions for each design. In the first model, zygomatic implant number 4 was placed in the defect region of the maxilla, while standard dental implants numbered 2, 4, and 6 were positioned at appropriate angles in the nondefect region (Fig. 2A). In the second model, zygomatic implant number 4 was again placed in the defect area of the maxilla, and standard dental implants numbered 2 and 4 were positioned at appropriate angles in the nondefect area (Fig.  2B). Finally, in the third model, zygomatic implant number 4 was placed at appropriate angles in both the defect and non-defect areas of the maxilla (Fig. 2C). After the implants were placed in the prepared models as planned, the restorations were completed. In each model, frameworks consisting of both resin and Co-Cr materials were prepared. For Co-Cr framework; standard dental implant connected with a height of $3 . 5 ~ \mathrm { m m }$ multi-unit $( 0 ^ { 0 } )$ abutments. Then, multi-unit and framework connection was provided with multi-unit abutment clinical screws. Zygomatic dental implant connected with and a height of $3 \ \mathrm { m m }$ multi-unit $( 0 ^ { 0 } )$ abutments. Then, multi-unit and framework connection was provided with multi-unit abutment clinical screws. For acrylic framework; standard and zygomatic dental implant connected with and a height of $3 \ \mathrm { m m }$ locator $( 0 ^ { 0 } )$ abutments. Then, locator and acrylic framework connection was provided with a male nylon cap and metal housing [2, 25]. Then, prosthetic models were created with maximum $2 \mathrm { m m }$ thickness porcelain layer on a Co-Cr framework [26, 27] and acrylic layer on an acrylic framework.
Fig. 2 A) Zygoma implant at number 4 in the defective area and dental implant at numbers 2-4-6 in the non-defective area B) Zygoma implant at number 4 in the defective area and dental implant at numbers 2–4 in the non-defective area C) Zygoma implant at number 4 in the defective and nondefective areas
Fig. 3 A) Mesh structure of the 3D model generated according to the FEA. B) Mesh structure of the 3D model of the superstructure on the frameworks generated according to the FEA.

Table 1 Mechanical properties of the materials used in modelling

<table><tr><td>Material</td><td>Young&#x27;s modulus (E) (MPa)</td></tr><tr><td>Cortical bone</td><td>0.30 [2,11]</td></tr><tr><td>Trabecular bone</td><td>0.30 [11]</td></tr><tr><td>Ti6AlV</td><td>0.30[2]</td></tr><tr><td>Acrylic resin (pmma)</td><td>0.30[2]</td></tr><tr><td>Titanium</td><td>0.35[2]</td></tr><tr><td>Co-Cr Alloy</td><td>0.33[27]</td></tr><tr><td>Porcelain</td><td>0.33 [26,27]</td></tr></table> structure of each model comprised a total of 1,273,408 nodes and 834,067 finite elements (Fig.  3). Finally, each mesh structure was modelled as isotropic, homogeneous, and linear elastic.


# Material properties

The mechanical properties of the materials used for each maxillary model and implant system were determined by the literature. At this stage, Young’s modulus (E), Poisson’s ratio (ν), and material density values obtained from the literature for cancellous bone, compact bone, dental bone, titanium implants, titanium abutments, titanium abutment screws, and zygomatic implants were assigned to match the physical properties of each structure. All specified materials were modelled as isotropic, homogeneous, and linear elastic. The mechanical properties of all materials used in the study were taken from previous studies and are detailed in Table 1.

# Mesh structure

The solid models obtained for the three scenarios were transferred to ANSYS Workbench software for finite element analysis, with meshing performed separately for each model. To achieve realistic results, careful attention was given to selecting the optimal size of the finite elements for the mesh structures and using the appropriate finite elements. Consequently, a convergence study was conducted on the element dimensions to increase the overall accuracy of the mesh structure, minimize the variations in the values and determine the optimal mesh size. In all models, mesh sizes were progressively reduced from coarse to fine until the stress values converged. Additionally, mesh refinements were applied in contact regions to enhance accuracy. Each finite element in the mesh structure was characterized by a Solid 92 element with a tetrahedral configuration consisting of 8 nodes. The mesh structure was created by combining finite elements sized at $0 . 0 7 5 \mathrm { m m }$ for the teeth, $1 \mathrm { m m }$ for the maxilla structure, $0 . 2 5 ~ \mathrm { m m }$ for the standard dental implants, and $0 . 2 5 ~ \mathrm { \ m m }$ for the zygomatic implant. Each finite element used was designed to accommodate displacement and rotation along the $\mathbf { x } , \mathbf { y } ,$ and $\mathbf { Z }$ axes. The mesh

# Loads and boundary conditions

Before proceeding to the FEA, the boundary conditions of the model were defined, and simulations were performed under different loading conditions. To simulate a realistic maxillary model, boundary conditions were assumed to be constant (zero displacement) at the junction of the maxilla (both the defect and non-defect regions) with the zygomatic bone. For the loading scenarios, a static force of $1 5 0 \mathrm { N }$ (to simulate bite load) was first applied to the defect area, then to the non-defect area, and finally to both areas separately at an angle relative to the occlusal surfaces (vertical plane). Subsequently, a static force of $1 5 0 ~ \mathrm { N }$ perpendicular to the occlusal surfaces (again simulating bite load) was applied to the defect area, the non-defect area, and finally to both areas separately [2, 11, 28]. Based on the previous study, the applied $1 5 0 ~ \mathrm { N }$ load was distributed to the premolar and molar teeth [29]. This load was distributed to 30 points, each consisting of $5 \mathrm { ~ N ~ }$ force. 5-point vertical loads were applied to the premolars and 10-point vertical loads were applied to the molars. The loads were distributed as $2 5 \ \mathrm { N }$ to the premolars and $5 0 ~ \mathrm { N }$ to the molars. The force was distributed to the central fossa and the side of the palatal cusp (functional cusp) facing the central fossa (Fig.  4). Finite element analyses were performed under these conditions and loadings, with maximum stress and deformation values for the maxillary structure and implants recorded. The results obtained were examined comparatively. The stress and deformation distribution of the maxillary structure following the analysis is shown in Fig. 5.

# Results

In this study, the distribution and magnitude of stresses on the bone were examined by applying loads to zygomatic and standard implants. Stresses were calculated as the maximum values of principal stress, defined as the maximum or minimum normal forces occurring in a loaded model, and von Mises stress, which indicates whether the material will yield or fracture. Three-dimensional loading simulations were conducted using FEA to calculate these stresses.

Understanding the stress magnitudes in the model and the regions where stresses are concentrated is significant during the design or decision-making phases. Based on the stress conditions, experts can make informed decisions regarding the materials to be used or the type of treatment, helping to prevent potential complications and improve patient outcomes.
Fig. 4 Occlusal and lateral view of the force applied to premolars and molars

Different implant models and loading conditions were created to examine various scenarios. Each scenario was analyzed separately using acrylic layer on acrylic framework and porcelain layer on CoCr framework and the results were compared. Table  2 provides details of the boundary conditions and loading conditions used in the analysis. The stress values obtained under the given model details and boundary conditions in Table  2 are compared in Fig. 6 for maximum principal stress and in Fig. 7 for maximum von Mises stress.

When examining Fig.  6 for the implant models, the greatest maximum principal stress value under all boundary conditions was observed in Model 3, while the smallest value was found in Model 1 when both porcelain layer on CoCr framework and acrylic layer on acrylic framework were used as prosthetic materials. Although the stress values for Models 2 and 3 are close to each other across all boundary conditions, the stress value for Model 1 is significantly lower than those of the other two models. Regarding the boundary conditions, the highest maximum principal stress value was recorded under the HL-D&ND (horizontal loading on the defective and non-defective areas) loading condition, while the lowest maximum principal stress value was noted under the VL-ND (vertical loading on the non-defective area) loading condition across all models. Additionally, using porcelain layer on CoCr framework as a prosthetic material slightly decreased the stress values compared to using acrylic layer on acrylic framework.
Fig. 5 Deformation shapes

Table 2 Details of analysis models and boundary conditions

<table><tr><td>Detail</td><td>Detail Name/Abbreviation</td><td>Definition</td></tr><tr><td rowspan="4">Analysis Models</td><td>Model 1</td><td>Zygoma implant at number 4in the defective area and dentalimplant at numbers 2-4-6 in the non-defective area</td></tr><tr><td>Model 2</td><td>Zygoma implant at number 4 in the defective area and dental implant at numbers 2-4 in the non-defective area</td></tr><tr><td>Model 3</td><td>Zygoma implant at number 4 in the defective and non-defective areas</td></tr><tr><td>VL-D</td><td>Vertical loading on the defective area</td></tr><tr><td rowspan="5">Boundary Conditions</td><td>VL-ND</td><td>Vertical loading on the non-defective area</td></tr><tr><td>HL-D</td><td>Horizontal loading on the defective area</td></tr><tr><td>HL-ND</td><td>Horizontal loading on the non-defective area</td></tr><tr><td>VL-D&amp;ND</td><td>Vertical loading on the defective and non-defective areas</td></tr><tr><td>HL-D&amp;ND</td><td>Horizontal loading on the defective and non-defective areas</td></tr></table>

VL; vertical loading, HL; horizontal loading, D; defective area, ND; non-defective area
Fig. 6 A) The maximum principal stress for the bone with porcelain layer on CoCr framework B) The maximum principal stress for the bone with acrylic layer on acrylic framework
Fig. 7 A) The maximum von Mises stress for the dental implant with porcelain layer on CoCr framework B) The maximum von Mises stress for the dental implant with acrylic layer on acrylic framework

When examining Fig.  7, it can be observed that the maximum von Mises stress values obtained in the implant models using both porcelain layer on CoCr framework and acrylic layer on acrylic framework as prosthetic materials are close and, in some cases, nearly identical under the same boundary conditions. Unlike the maximum principal stress values, the maximum von Mises stress values did not exhibit significant differences under different boundary conditions, nor did they show substantial variations when the loading condition was altered. Furthermore, using acrylic layer on acrylic framework instead of porcelain layer on CoCr framework as the prosthetic material slightly increased the stress values in the models.

# Discussion

Excessive stress between the implant and bone is a significant factor contributing to bone loss around the implant and failures in osseointegration. Therefore, estimating the scenarios in which stress levels will peak is crucial for the success of implant-supported prostheses [11]. In the present study, prosthetic models containing various configurations of zygomatic and dental implants were designed to address unilateral maxillary defects using the FEA method. It was found that increasing the number of dental implants applied to the non-defective area resulted in lower maximum principal stress values; however, there was no significant difference between the models regarding von Mises stress values.

FEA was employed in the current study because it enables the estimation of stress values between the implant and the bone, while also facilitating the modelling of various prosthetic designs. The accuracy of the tests conducted in FEA studies is influenced by the properties of the materials, interface definitions, geometries, and applied forces [11]. Consequently, the modelling in this study was based on data obtained from a real CT scan. Additionally, to better reflect real-world conditions, the obturator prosthesis was modelled, and loads were applied directly to it. The maximum principal stress and von Mises stress values are the most commonly used metrics for evaluating stress distribution on bone. The maximum principal stress indicates the stress concentrated in a specific region, while the von Mises stress value allows for the assessment of material yielding and failure [30]. Therefore, both stress values were evaluated in the current study.

The number of implants used in implant-supported prostheses and their placement significantly affect the stress values between the implant and the bone, as well as the overall success of the prosthesis [31]. In the present study, three different models were created, revealing that the highest maximum principal stress value was observed in Model 3 (with one zygomatic implant placed in both the defected and non-defective areas), while the lowest value was found in Model 1 (with one zygomatic implant in the defected area and three dental implants in the non-defective area). The stress values in Models 2 (one zygomatic implant in the defected area and two dental implants in the non-defective area) and 3 were close to each other, whereas the stress value in Model 1 was considerably lower than in the other two models.

In contrast, Akay et al. [2] planned three different implant-supported locator attachment prostheses for Aramany Class 4 maxillary defects and found that, unlike this study, the use of a zygomatic implant in the non-defective area reduced the maximum principal stress values. They also reported that using a zygomatic implant in a non-defective area was more advantageous than employing one or two dental implants with locator attachments [2].

Wang et al. [29] investigated the retention provided by clasps and the resistance of abutments to excessive torque forces by creating models of unilateral maxillary defects using a conventional prosthesis, one zygomatic implant, and two zygomatic implants. The results of their study indicated that the stress values in the models with zygomatic implants were significantly lower than those in the model with a conventional prosthesis, with the lowest stress value observed in the model featuring two zygomatic implants. They concluded that zygomatic implantsupported prostheses are effective for the restoration of unilateral maxillary defects [29].

Freedman et al. [32] recorded von Mises stress values in their study investigating the effect of alveolar bone support on the stress distribution of zygomatic implants placed in the extra-sinus position. As a result of this study, they found that less stress occurred in the model without a maxillary defect and that the support provided by the alveolar bone was beneficial for zygomatic implants [33]. In the present study, the maximum von Mises stress values obtained in different implant models created under the same boundary conditions were found to be close to each other and, in some cases, almost equal.

Korkmaz et al. [11] reported in their study that they created four different bar-retained prosthesis models supported by zygomatic and dental implants in the presence of a unilateral maxillary defect. They found that the use of zygomatic implants in the non-defective area reduced the von Mises stress value and that increasing the number of dental implants in the non-defective area did not reduce the highest stress value. In the present study, the von Mises stress values in models prepared using zygomatic implants or different numbers of dental implants in the non-defective area were found to be close to each other, even when the direction of the applied force and the area where it was applied was changed.

The maximum bite force in patients with osseointegrated implants has been reported as $1 4 4 . 4 \mathrm { N }$ [34]. Therefore, in many studies, a force of $1 5 0 ~ \mathrm { N }$ has been applied to simulate the actual maximum bite force [2, 11, 29].

In the present study, a force of $1 5 0 \mathrm { N }$ was applied to the models. Additionally, the direction of the applied force is also important. Therefore, in this study, both vertical and lateral forces were applied to reflect chewing forces more realistically.

In the present study, when evaluated according to the forces applied to the models, the highest maximum principal stress value was observed when horizontal force was applied simultaneously to the defected and non-defective areas, while the lowest value was observed when vertical force was applied to the non-defective area. Additionally, when the loading conditions were changed in the models, the maximum von Mises stress values obtained did not show significant differences, similar to the maximum principal stress values. Unlike this study, Korkmaz et al. [11] found the lowest von Mises stress value in models where they placed zygomatic and dental implants in the non-defective area when vertical force was applied to that area. They also found similar values in models where vertical force was applied separately to the defected and non-defective areas in the model where they applied only dental implants to the non-defective area, while they found higher von Mises stress values when they applied vertical force simultaneously to both the defected and non-defective areas [11].

Akay et al. [2] found the highest stress value when force was applied to both sides in the model where one dental implant was placed in the non-defective area, while the lowest stress value was found in the model where one zygomatic implant was placed in the non-defective area. They reported that the distribution of stresses on the prostheses could be more rational with the help of zygomatic implants, which could distribute the stresses to each part of the maxilla [2].

Varghese et al. [3] applied two types of treatment methods in a severely atrophic edentulous maxilla model. In the first model, one conventional and one zygomatic implant was placed in each quadrant, while in the second model, two zygomatic implants were placed bilaterally in each quadrant. A vertical force of $1 5 0 \mathrm { N } .$ , a lateral force of $5 0 \mathrm { N }$ , and an occlusal force of $3 0 0 \ \mathrm { N }$ were applied to the models. When vertical force was applied, the stress was distributed more widely in the model with conventional implants. However, when lateral force was applied, significantly higher stress was determined in the model with conventional implants compared to the other model. When vertical and lateral forces were applied simultaneously, the highest von Mises stress value was found in the model with four zygomatic implants. In the present study, the highest maximum principal stress value in the model with zygomatic implants placed in the non-defective area was found when horizontal force was applied simultaneously to both the defected and non-defective areas. Although the von Mises value was not significantly different among the models, it was slightly higher in this model.

After implant placement, different prosthetic restorations, such as all-acrylic and metal framework-supported options, can be applied for temporary or final prostheses [35]. The framework materials may be an important factor in stress transmission to the implant-bone connection area [36]. Additionally, using all-acrylic prosthetic restorations has shown the most prosthodontic problems, such as fractures in the prosthesis [35]. In a previous study, the stress distribution of frameworks in different prosthodontic concepts (All-on-4 and All-on-6) was compared using a 3D FEA study. They concluded that stiffer framework materials (CoCr and Zr) decreased stress levels in different areas and exhibited the most suitable biomechanical behaviour. Furthermore, they noted that the titanium framework performed poorly in the All-on-4 prosthesis concept [36, 37]. In the present study, the use of a prosthesis made using an acrylic layer on acrylic framework instead of a prosthesis made using porcelain layer on Co-Cr framework as a material slightly increased both the maximum principal stress values and the von Mises stress values. In comparison with the current study, Arınç et al. [38] found similar results. They used FEA to evaluate the effects of prosthesis material on the stress levels in cortical bone, trabecular bone, and implants. Their findings showed that zirconia-reinforced polymethyl methacrylate (ZRPMMA; Poisson’s ratio (v): 0.3, Elastic modulus: $3 . 0 5 \mathrm { \ G P a }$ ) increased the maximum principal stress and von Mises stress values in implants and bone tissue more than Co-Cr and $Z \mathbf { r }$ while having the lowest von Mises stress value in the framework. When evaluated in terms of the materials used, although the Poisson ratios are the same in this study and Arınç et al. [36, 38], there is a slight difference in the elastic moduli.

There are some limitations to this study. First, muscle forces were not applied while vertical and horizontal forces were applied. The force during chewing could have been reflected more realistically by incorporating muscle forces. Second, all implants were assumed to be $1 0 0 \%$ osseointegrated. Another limitation is that all materials were assumed to be homogeneous, linearly elastic, and isotropic. While these results may help understand reallife conditions, more studies are needed.

# Conclusions

Within the limits of this study, when both porcelain layer on Co-Cr framework and acrylic layer on acrylic framework were used, the highest maximum principal stress value was observed in the model with a single zygomatic implant applied to the non-defective area, while the lowest value was observed in the model with three dental implants placed in the non-defective area. In all models, the highest maximum principal stress value was obtained when horizontal force was applied simultaneously to both the defected and non-defective areas, while the lowest value was found when vertical force was applied to the non-defective area. When both porcelain layer on Co-Cr framework and acrylic layer on acrylic framework were used, the von Mises stress values were found to be close to each other across the models and under different loading conditions.

# Acknowledgements

This study has been supported by the Recep Tayyip Erdoğan University Development Foundation (Grant number: 02024011007155).

# Author contributions

Planning of the study: HY, MB, MA, MY, ZY; Methodology: HY, MB, MA, MY, ZY, AD, MEÖ, $\ S \ O _ { \ O _ { \prime } }$ Analysis: MY, AD, MEÖ, $\ S \dot { \bigcirc } ;$ Evaluation of the results: HY, MB, MA, MY; Research and verification: AD, MY, MEÖ, $\ S \dot { \bigcirc } ;$ Obtaining and examining the radiographic image data required for analysis: MEN; Visualization: HY, MY, EUY; Writing: HY, MB, MA, MY; Review and editing: HY, MB, MA, MY, EUY, MEN; All authors read and approved the final manuscript.

# Funding

There is no funding.

# Data availability

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request.

# Declarations

# Ethical approval and consent to participate

Ethical approval was obtained from the Non-Invasive Clinical Research Ethics Committee of Recep Tayyip Erdoğan University (Decision no: 2024/56). In our study, retrospective panoramic radiography archives were scanned and examined. We obtained institutional permission to use data from patients with these radiographs. All procedures performed in the study were in accordance with the ethical standards of the institutional and/or national research committee and the 1975 Declaration of Helsinki, revised in 2013. Informed consent was obtained from all participants included in the study.

# Human ethics

The study does not include samples of human tissues. Only radiographic images of the past were used. Institutional permission and ethical approval were obtained for this.

Consent for publication Not Applicable.

# Competing interests

The authors declare no competing interests.

# Author details

1 Department of Periodontology, Faculty of Dentistry, Recep Tayyip
Erdoğan University, Rize 53020, Turkey
2 Department of Civil Engineering, Recep Tayyip Erdoğan University,
Rize 53100, Turkey
3 Biomedical Engineering MSc Program, Recep Tayyip Erdoğan University,
Rize 53100, Turkey
4 Department of Biomedical Engineering, Kocaeli University, İzmit,
Kocaeli 41380, Turkey
5 Department of Prosthodontics, Faculty of Dentistry, Recep Tayyip
Erdoğan University, Rize, Turkey
6 Department of Oral and Maxillofacial Radiology, Faculty of Dentistry,
Recep Tayyip Erdoğan University, Rize, Turkey
7 Faculty of Engineering and Architecture, Recep Tayyip Erdoğan
University, Rize 53100, Turkey
8 Faculty of Fisheries, Recep Tayyip Erdoğan University, Rize 53100, Turkey
9 Department of Civil Engineering, Cankiri Karatekin University,
Çankırı 18100, Turkey
10Department of Prosthodontics, Faculty of Dentistry, Ataturk University,
Erzurum, Turkey

Received: 8 October 2024 / Accepted: 9 January 2025
Published online:19 January 2025

# References

1. Özdemir H, Hülagü B. Three-dimensional Finite Element Analysis of Zygoma Implants in a patient with a Maxillary defect. Int J Innovative Res Reviews. 2024;8(1):6–11.
2. Akay C, Yaluğ S. Biomechanical 3-dimensional finite element analysis of obturator protheses retained with zygomatic and dental implants in maxillary defects. Med Sci Monitor: Int Med J Experimental Clin Res. 2015;21:604. https://doi.org/10.12659/MSM.892680.
3. Varghese KG, Kurian N, Gandhi N, Gandhi S, Daniel AY, Thomas HA et al. Three-dimensional finite element analysis of zygomatic implants for rehabilitation of patients with a severely atrophic maxilla. The Journal of Prosthetic Dentistry, 2023; 129(4): 597. e1-597. https://doi.org/10.1016/j.prosdent.2023.0 1.012
4. Tezerişener HA, Özalp Ö, Altay MA, Sindel A. Comparison of stress distribution around all-on-four implants of different angulations and zygoma implants: a 7-model finite element analysis. BMC Oral Health. 2024;24(1):176. https://doi. org/10.1186/s12903-023-03761-x.
5. Gracher AHP, Moura MB, Peres PS, Thome G, Padovan LEM, Trojan LC. Full arch rehabilitation in patients with atrophic upper jaws with zygomatic implants: a systematic review. Int J Implant Dentistry. 2021;7:1–9. https://doi.org/10.118 6/s40729-021-00297-z.
6. Corvello PC, Montagner A, Batista FC, Smidt R, Shinkai RS. Length of the drilling holes of zygomatic implants inserted with the standard technique or a revised method: a comparative study in dry skulls. J Cranio-Maxillofacial Surg. 2011;39(2):119–23.
7. Petrungaro PS, Gonzales S, Villegas C, Yousef J, Arango A. A retrospective study of a Multi-center Case Series of 452 zygomatic implants placed over 5 years for treatment of severe Maxillary Atrophy. Compendium. 2020;41(4):232.
8. Schmidt BL, Pogrel MA, Young CW, Sharma A. Reconstruction of extensive maxillary defects using zygomaticus implants. J Oral Maxillofac Surg. 2004;62:82–9. https://doi.org/10.1016/j.joms.2004.06.027.
9. Parel SM, Branemark P, Ohrnell LO, Svensson B. Remote implant anchorage for the rehabilitation of maxillary defects. J Prosthet Dent. 2001;86(4):377–81. https://doi.org/10.1067/mpr.2001.118874.
10. Kreissl ME, Heydecke G, Metzger MC, Schoen R. Zygoma implant-supported prosthetic rehabilitation after partial maxillectomy using surgical navigation: a clinical report. J Prosthet Dent. 2007;97(3):121–8. https://doi.org/10.1016/j.p rosdent.2007.01.009.
11. Korkmaz FM, Korkmaz YT, Yaluğ S, Korkmaz T. Impact of dental and zygomatic implants on stress distribution in maxillary defects: a 3-dimensional finite element analysis study. J Oral Implantology. 2012;38(5):557–67. https://doi.or g/10.1563/AAID-JOI-D-10-00111.
12. Rathod DK, Chakravarthy C. Stress distribution of the zygomatic implants in post-mucormycosis case: a finite element analysis. J Oral Maxillofac Surg. 2023;22(3):695–701.
13. Logan DL. A first course in the finite element method. Evelyn Veitch, Harlan James. Univ Wisconsin–Platteville Thomson 4. 2011.
14. Uzun Yaylacı E, Özdemir ME, Güvercin Y, Öztürk Ş, Yaylacı M. Analysis of the mechano-bactericidal effects of nanopatterned surfaces on implant-derived bacteria using the FEM. 2023; 567–77. https://doi.org/10.12989/anr.2023.15.6. 567
15. Uzun Yaylaci E, Yaylaci M, Özdemir ME, Terzi M, Öztürk Ş. Analyzing the mechano-bactericidal effect of nano-patterned surfaces by finite element method and verification with artificial neural networks. Adv nano Res. 2023;15(2):165–74.
16. Güvercin Y, Abdioğlu AA, Dizdar A, Uzun Yaylacı E, Yaylacı M. Suture button fixation method used in the treatment of syndesmosis injury: a biomechanical analysis of the effect of the placement of the button on the distal tibiofibular joint in the mid-stance phase with finite elements method. Injury. 2022;53(7):2437–45. https://doi.org/10.1016/j.injury.2022.05.037.
17. Güvercin Y, Yaylacı M, Dizdar A, Kanat A, Uzun Yaylacı E, Ay S, et al. Biomechanical analysis of odontoid and transverse atlantal ligament in humans with ponticulus posticus variation under different loading conditions: finite element study. Injury. 2022;53(12):3879–86. https://doi.org/10.1016/j.injury.20 22.10.003.
18. Güvercin Y, Yaylacı M, Ölmez H, Özdemir ME, Dizdar A, Uzun Yaylacı E. Finite element analysis of the mechanical behavior of the different angle hip femoral stem. 2022;29–46. https://doi.org/10.12989/bme.2022.6.1.029
19. Zagane MES, Abdelmadjid M, Yaylacı M, Abderahmen S, Uzun Yaylacı E. Finite element analysis of the femur fracture for a different total hip prosthesis (Charnley, Osteal, and Thompson). Structural Engineering and Mechanics, An Int’l Journal, 2023; 88(6):583–588. https://doi.org/10.12989/sem.2023.88.6.583
20. Moulgada A, Zagane MES, Yaylacı M, Djafar AK, Abderahmane S, Öztürk Ş, et al. Comparative study by the finite element method of three activities of a wearer of total hip prosthesis during the postoperative period. Struct Eng Mech Int’l J. 2023;87(6):575–83. https://doi.org/10.12989/sem.2023.87.6.575.
21. Benouis A, Zagane MES, Moulgada A, Yaylacı M, Kaci DA, Terzi M, et al. Finite element analysis of the behavior of elliptical cracks emanating from the orthopedic cement interface in total hip prostheses. Struct Eng Mech. 2024;89(5):539. https://doi.org/10.12989/sem.2024.89.8.539.
22. Nişanci GN, Güvercin Y, Ateş SM, Ölmez H, Uzun Yaylacı E, Yaylacı M. Investigation of the effect of different prosthesis designs and numbers on stress, strain and deformation distribution. Int J Eng Appl Sci. 2020;12(4):138–52. https://d oi.org/10.24107/ijeas.816227.
23. Terzi M, Güvercin Y, Ateş SM, Sekban DM, Yaylacı M. Effect of different abutment materials on stress distribution in peripheral bone and dental implant system. Sigma J Eng Nat Sci. 2020;38(3):1495–507.
24. Kurt A, Yaylacı M, Dizdar A, Naralan ME, Yaylacı EU, Öztürk Ş, et al. Evaluation of the effect on the permanent tooth germ and the adjacent teeth by finite element impact analysis in the traumatized primary tooth. Int J Pediatr Dent. 2024. https://doi.org/10.1111/ipd.13183.
25. Over LM, Eric D. Interdisciplinary prosthetic rehabilitation following bilateral maxillectomy with total upper lip and unilateral zygoma resection: a clinical report. J Prosthet Dent. 2022;131:341–5. https://doi.org/10.1016/j.prosdent.20 22.03.038.
26. Elias A, Banu RF, Vaidyanathan AK, Padmanabhan TV. A comparative finite element analysis of titanium, poly-ether-etherketone, and zirconia abutment on stress distribution around maxillary anterior implants. Dent Res J (Isfahan). 2024;6:21. PMID: 38807658; PMCID: PMC11132231.
27. Tekin S, Değer Y, Demirci F. Evaluation of the use of PEEK material in implantsupported fixed restorations by finite element analysis. Niger J Clin Pract. 2019;22(9):1252–8. https://doi.org/10.4103/njcp.njcp_144_19.
28. Akay C, Yaluğ S, Dalkız M. Effects of dental and zygomatic implants on stress distribution in zygomatic bone. Suleyman Demirel Univ J Eng Sci Des. 2014;2(3):253–9. SI:BioMechanics.
29. Wang M, Qu X, Cao M, Wang D, Zhang C. Biomechanical three-dimensional finite element analysis of prostheses retained with/without zygoma implants in maxillectomy patients. J Biomech. 2013;46(6):1155–61. https://doi.org/10.1 016/j.jbiomech.2013.01.004.
30. Yemineni BC, Mahendra J, Nasina J, Mahendra L, Shivasubramanian L, Perika SB. Evaluation of maximum principal stress, Von mises stress, and deformation on surrounding mandibular bone during insertion of an implant: a three-dimensional finite element study. Cureus. 2020;12(7):e9430. https://doi. org/10.7759/cureus.9430.
31. Geng JP, Tan KB, Liu GR. Application of finite element analysis in implant dentistry: a review of the literature. J Prosthet Dent. 2001;85(6):585–98. https:/ /doi.org/10.1067/mpr.2001.115251.
32. Freedman M, Ring M, Stassen LFA. Effect of alveolar bone support on zygomatic implants in an extra-sinus position—a finite element analysis study. Int J Oral Maxillofac Surg. 2015;44(6):785–90. https://doi.org/10.1016/j.ijom.2015. 01.009.
33. Freedman M, Ring M, Stassen LFA. Effect of alveolar bone support on zygomatic implants: a finite element analysis study. Int J Oral Maxillofac Surg. 2013;42(5):671–6. https://doi.org/10.1016/j.ijom.2012.12.006.
34. Haraldson T, Carlsson GE. Bite force and oral function in patients with osseointegrated oral implants. Eur J Oral Sci. 1977;85(3):200–8. https://doi.org/10.1 111/j.1600-0722.1977.tb00554.x.
35. Agliardi E, Romeo D, Panigatti S, Nobre MA, Malo P. Immediate full-arch rehabilitation of the severely atrophic maxilla supported by zygomatic implants: a prospective clinical study with minimum follow-up of 6 years. Int J Oral Maxillofac Surg. 2017;46(12):1592–9. https://doi.org/10.1016/j.ijom.2017.05.023.
36. Bacchi A, Consani RLX, Mesquita MF, Dos Santos MBF. Effect of framework material and vertical misfit on stress distribution in implant-supported partial prosthesis under load application: 3-D finite element analysis. Acta Odontol Scand. 2013;71(5):1243–9. https://doi.org/10.3109/00016357.2012.757644.
37. Bhering CLB, Mesquita MF, Kemmoku DT, Noritomi PY, Consani RLX, Barao VAR. Comparison between all-on-four and all-on-six treatment concepts and framework material on stress distribution in atrophic maxilla: a prototyping guided 3D-FEA study. Mater Sci Engineering: C. 2016;69:715–25. https://doi.o rg/10.1016/j.msec.2016.07.059.
38. Arinc H. Implant-supported fixed partial prostheses with different prosthetic materials: a three-dimensional finite element stress analysis. Implant Dent. 2018;27(3):303–10. https://doi.org/10.1097/ID.0000000000000750.

# Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
