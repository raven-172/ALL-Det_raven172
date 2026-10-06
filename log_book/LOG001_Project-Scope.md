# Research Reading Log

*Computer Vision for Acute Lymphoblastic Leukemia*

**Entry:** 1  
**Date:** 6 October 2026

This entry reviews five papers on computer vision approaches to acute lymphoblastic leukemia (ALL). It examines image classification, cell detection, transfer learning, detector architectures, and computational efficiency, with particular attention to dataset limitations and the interpretation of reported performance.

## Paper 1 — CNN and YOLO Models for ALL Image Analysis

### Research Focus and Approach

Paper 1 reports results for ALL image analysis using computer vision models, including a convolutional neural network (CNN), YOLOv5s, YOLOv5m, YOLOv5 without pretrained weights, YOLOv6, and YOLOv7. The CNN performs image classification, whereas all five YOLO configurations perform object detection.

### Reported Results

**Table 1. Performance of CNN and YOLO models**

| Model | Accuracy | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 | Inference latency (ms) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| CNN | 99.22% | NS | NS | NS | NS | NS |
| YOLOv5s | NS | 0.885 | 0.985 | 0.972 | 0.832 | 12.3 |
| YOLOv5m | NS | 0.936 | 0.955 | 0.981 | 0.861 | 21.9 |
| YOLOv5 (no pretrained weights) | NS | 0.679 | 0.970 | 0.853 | 0.642 | 22.0 |
| YOLOv6 | NS | NS | NS | 0.644\* | 0.548\* | 16.0 |
| YOLOv7 | NS | 0.554 | 1.000 | 0.737 | 0.608 | 42.7 |

**Note:** NS = not specified in the original log. Accuracy is expressed as a percentage; precision, recall, and mAP retain their reported decimal form. The asterisks attached to the YOLOv6 values are retained, but their meaning is not specified in the log.

### Critical Observations

The results provide information on the effectiveness of YOLO models in processing ALL-IDB1 images and identifying the classes represented in the dataset. However, the evaluation and comparison of models require reconsideration because the training conditions differ, particularly for YOLOv5 without pretrained weights. The evaluation measures and details of the CNN model are also insufficiently specified.

The results are affected by the annotation limitations of ALL-IDB1, which provides only the center locations of diseased cells. Applying YOLO therefore requires additional, manually created annotations, which may lead to poorer model performance. The models should be evaluated on a larger and more realistic dataset.

## Paper 2 — Histopathology Transfer Learning and Lightweight Classification

### Research Focus and Approach

Paper 2 addresses binary classification of diseased and non-diseased cells using ALL-IDB2. It applies transfer learning from the Atlas of Digital Pathology (ADP), using a histopathology dataset with similarities to the target dataset to improve classification performance.

The study organizes histopathology labels into three levels of increasing detail:

- **Level 1** describes a broad tissue type, such as Nervous.
- **Level 2** describes a more specific cell or tissue group, such as Neuroglial Cells.
- **Level 3** provides the most detailed description, such as Undifferentiated Neuroglial Cells.

Each level is used to pretrain a separate CNN, which is then transferred to the classification of cells as Normal or Lymphoblast on ALL-IDB2. The study also seeks to improve computational efficiency by designing a lighter classification model with fewer parameters. It proposes a Local Binary Convolutional Module (LBCM).

### Reported Results

**Table 2. Classification performance of ALLNet configurations**

| ALLNet configuration | Histopathology level | Accuracy (%) | Standard deviation (%) |
| --- | :---: | :---: | :---: |
| ALLNet ResNet18-L1 | Level 1 | 97.85 | 0.58 |
| ALLNet ResNet18-L2 | Level 2 | 97.54 | 1.57 |
| ALLNet ResNet18-L3 | Level 3 | 97.23 | 2.04 |
| ALLNet ResNet34-L1 | Level 1 | 95.38 | 5.01 |
| ALLNet ResNet34-L2 | Level 2 | **98.46** | **0.84** |
| ALLNet ResNet34-L3 | Level 3 | 98.00 | 1.86 |

**Dataset and task:** All six configurations use ADP Histopathology for pretraining and ALL-IDB2 as the target dataset. The classification task is Normal versus Lymphoblast. L1, L2, and L3 in the model names correspond to histopathology Levels 1, 2, and 3, respectively.

**Table 3. Comparison of HistoTNet and ALLNet with ResNet34 at Level 2**

| Metric | HistoTNet ResNet34-L2 | ALLNet ResNet34-L2 |
| --- | :---: | :---: |
| Classification Accuracy (%) | 96.62 | **98.46** |
| Learnable Parameters | 21,285,698 | **342,082** |
| Model Size | 83 MB | **5 MB** |
| Parameter Reduction | — | **~62×** |

### Critical Observations

The study was evaluated on the small ALL-IDB2 dataset containing only 260 cropped single-cell images. The task was limited to binary classification between normal cells and lymphoblasts, without detecting cells in whole blood-smear images or distinguishing ALL subtypes. Generalization to independent clinical datasets was not evaluated.

## Paper 3 — Detection Workflows and Challenges in Blood Smear Images

### Research Focus and Detection Workflows

Paper 3 categorizes CNN-based object detectors into two groups according to their detection workflow:

**Two-stage detectors** first identify candidate regions and then classify and refine those regions. By narrowing the candidate regions before analyzing each region in detail, these detectors generally achieve greater detection accuracy, as described in the paper.

**One-stage detectors** directly predict object classes and locations without a separate region proposal stage. This simpler workflow reduces latency and makes real-time inference more achievable.

### Comparison of Detector Characteristics

The paper describes two-stage detectors as having an accuracy advantage over one-stage detectors. However, their architectures are more complex, inference is generally slower, and they require more computational resources. One-stage detectors are more suitable for systems that require fast inference.

### Relevance to Blood Smear Images

An especially important limitation of one-stage detectors in blood-smear images is the localization of small objects. The paper identifies limitations of YOLO when objects are small, multiple objects are located close together, or object boundaries are difficult to determine. These challenges are directly relevant to blood cells, which can appear small and clustered within a smear.

## Paper 4 — Hospital Data and Classification of ALL Cell Types

### Research Focus and Reported Results

Paper 4 provides a more realistic and detailed evaluation using a dataset collected from a hospital and defining cell categories for classification. The paper presents its results clearly and reports high performance.

### Critical Observations

**Unusually perfect results.** CNN, Xception, and MobileNetV2 all achieve 100% accuracy, precision, recall, and F1-score. These results therefore require cautious interpretation.

**Limited patient diversity.** The dataset contains 3,256 images from only 89 patients. A large number of images does not necessarily indicate substantial patient diversity.

**Unclear data splitting.** The paper states that the dataset was divided into training and testing sets, but it does not clearly describe a patient-level split. The possibility that images from the same patient appear in both sets therefore cannot be ruled out.

**No external validation.** The study does not evaluate performance using an independent hospital or dataset. Generalizability has therefore not been demonstrated.

**Methodological inconsistency.** The feature extraction section refers to “segmented chest X-ray pictures,” although the study uses blood-smear images. This suggests an inconsistency in the methodological description.

**Limited interpretability.** The paper classifies cells as Benign, Early Pre-B, Pre-B, and Pro-B, but does not explain which morphological features distinguish the three malignant classes.

## Paper 5 — Ghost Modules for YOLO Detection of ALL Subtypes

### Research Focus and Approach

Paper 5 provides a newer and more detailed evaluation of YOLO models by including ALL subtype categories. Its primary focus is to improve computational efficiency, particularly by reducing the number of model parameters through a Ghost Module.

The paper argues that feature extraction in earlier models produces many feature maps containing redundant information. The Ghost Module reduces expensive convolutional operations by learning a compact set of intrinsic feature maps and generating additional related features through simple operations. This reduces the number of parameters and floating-point operations (FLOPs), with only a minor reduction in detection performance, as described in the paper.

### Reported Detection Results

**Table 4. Detection performance for overall ALL detection**

| Metric | YOLOv4 Original | YOLOv5 Original | YOLOv4 + GhostNet | YOLOv5 + GhostNet |
| --- | :---: | :---: | :---: | :---: |
| Precision (%) | 89.5 | 88.4 | 88.9 | 85.5 |
| Recall (%) | 89.5 | 88.6 | 86.7 | 87.0 |
| F1-score (%) | 89.5 | 88.3 | 87.6 | 86.1 |
| mAP@0.5 (%) | **93.2** | 92.7 | 90.9 | 91.5 |
| mAP@0.5:0.95 (%) | 65.9 | **66.2** | 65.0 | 65.2 |

**Table 5. Detection performance for the L1 subtype**

| Metric | YOLOv4 Original | YOLOv5 Original | YOLOv4 + GhostNet | YOLOv5 + GhostNet |
| --- | :---: | :---: | :---: | :---: |
| Precision (%) | 89.6 | **93.0** | 90.3 | 87.4 |
| Recall (%) | 95.0 | 93.3 | 94.0 | **95.7** |
| F1-score (%) | 92.1 | **92.9** | 92.0 | 90.9 |
| mAP@0.5 (%) | 96.3 | **96.8** | 94.6 | 95.5 |
| mAP@0.5:0.95 (%) | 68.3 | **71.3** | 67.7 | 69.0 |

**Table 6. Detection performance for the L2 subtype**

| Metric | YOLOv4 Original | YOLOv5 Original | YOLOv4 + GhostNet | YOLOv5 + GhostNet |
| --- | :---: | :---: | :---: | :---: |
| Precision (%) | **87.1** | 79.0 | 83.9 | 79.1 |
| Recall (%) | 77.6 | **79.5** | 70.3 | 69.6 |
| F1-score (%) | **81.9** | 75.4 | 73.6 | 72.0 |
| mAP@0.5 (%) | **85.4** | 83.6 | 80.9 | 81.4 |
| mAP@0.5:0.95 (%) | 62.4 | 60.3 | 60.5 | **63.7** |

**Table 7. Detection performance for the L3 subtype**

| Metric | YOLOv4 Original | YOLOv5 Original | YOLOv4 + GhostNet | YOLOv5 + GhostNet |
| --- | :---: | :---: | :---: | :---: |
| Precision (%) | 91.7 | **93.2** | 92.5 | 90.1 |
| Recall (%) | **96.0** | 92.9 | 95.8 | 95.6 |
| F1-score (%) | 93.8 | 92.9 | **94.1** | 92.4 |
| mAP@0.5 (%) | 97.7 | **97.9** | 97.4 | 97.6 |
| mAP@0.5:0.95 (%) | 66.9 | **67.1** | 67.0 | 67.0 |

### Reported Computational Efficiency

**Table 8. Computational efficiency of the original and GhostNet variants**

| Metric | YOLOv4 Original | YOLOv5 Original | YOLOv4 + GhostNet | YOLOv5 + GhostNet |
| --- | :---: | :---: | :---: | :---: |
| GFLOPs | 16.3 | 15.8 | **9.8** | **9.6** |
| Parameters | 7,210,824 | 7,018,216 | **4,692,312** | **4,588,184** |
| Pre-processing (ms) | 0.56 | 0.62 | 0.64 | 0.88 |
| Inference (ms) | 5.74 | 4.82 | **3.94** | 5.08 |
| NMS (ms) | 2.82 | 3.32 | **2.44** | 3.08 |
| Total Detection Time (ms) | 9.12 | 8.76 | **7.02** | 9.04 |
| Approx. Parameter Reduction | — | — | ~35% | ~35% |
| Approx. GFLOPs Reduction | — | — | ~40% | ~40% |
| Reported Performance Difference vs Original | — | — | ~1.4% | ~2.4% |

**Note:** GFLOPs = billions of floating-point operations; NMS = non-maximum suppression. The reported performance differences relative to the original models are retained as approximately 1.4% and 2.4%. The log does not identify the associated metric or clarify whether these values refer to relative percentages or percentage points.

## References

1. **Paper 1.** Emma Chen, Rory Liao, Mikhail Y. Shalaginov, and Tingying Helen Zeng (2022). *Real-time Detection of Acute Lymphoblastic Leukemia Cells Using Deep Learning*. In *2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*, pp. 3788–3790. DOI: `10.1109/BIBM55620.2022.9995131`.

2. **Paper 2.** Angelo Genovese (2022). *ALLNet: Acute Lymphoblastic Leukemia Detection Using Lightweight Convolutional Networks*. In *2022 IEEE 9th International Conference on Computational Intelligence and Virtual Environments for Measurement Systems and Applications (CIVEMSA)*. DOI: `10.1109/CIVEMSA53371.2022.9853691`.

3. **Paper 3.** Tanzilal Mustaqim, Chastine Fatichah, and Nanik Suciati (2023). *Deep Learning for the Detection of Acute Lymphoblastic Leukemia Subtypes on Microscopic Images: A Systematic Literature Review*. *IEEE Access*, 11, 16108–16127. DOI: `10.1109/ACCESS.2023.3245128`.

4. **Paper 4.** Naveen Ghorpade, Ajay Sudhir Bale, Santosh Suman, Divya V, Suraj Mandal, and Parashivamurthy C (2024). *Acute Lymphoblastic Leukemia Detection Employing Deep Learning and Transfer Learning Techniques*. In *2024 International Conference on Advances in Computing, Communication and Applied Informatics (ACCAI)*. DOI: `10.1109/ACCAI61061.2024.10602062`.

5. **Paper 5.** Tanzilal Mustaqim, Chastine Fatichah, and Nanik Suciati (2022). *Modification of YOLO with GhostNet to Reduce Parameters and Computing Resources for Detecting Acute Lymphoblastic Leukemia*. In *2022 International Conference on Advanced Computer Science and Information Systems (ICACSIS)*, pp. 167–172. DOI: `10.1109/ICACSIS56558.2022.9923484`.

## Paper Files

- **Paper 1:** [Real-time Detection of Acute Lymphoblastic Leukemia Cells Using Deep Learning](https://github.com/raven-172/ALL-Det_raven172/blob/main/docs/paper1.pdf)
- **Paper 2:** [ALLNet: Acute Lymphoblastic Leukemia Detection Using Lightweight Convolutional Networks](https://github.com/raven-172/ALL-Det_raven172/blob/main/docs/paper2.pdf)
- **Paper 3:** [Deep Learning for the Detection of Acute Lymphoblastic Leukemia Subtypes on Microscopic Images: A Systematic Literature Review](https://github.com/raven-172/ALL-Det_raven172/blob/main/docs/paper3.pdf)
- **Paper 4:** [Acute Lymphoblastic Leukemia Detection Employing Deep Learning and Transfer Learning Techniques](https://github.com/raven-172/ALL-Det_raven172/blob/main/docs/paper4.pdf)
- **Paper 5:** [Modification of YOLO with GhostNet to Reduce Parameters and Computing Resources for Detecting Acute Lymphoblastic Leukemia](https://github.com/raven-172/ALL-Det_raven172/blob/main/docs/paper5.pdf)
