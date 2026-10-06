- Paper 1 cung cấp kết quả xử lý hình ảnh của ALL thông qua các mô hình thị giác máy tính, cụ thể là bao gồm CNN, YOLOv5s, YOLOv5m, YOLOv5, YOLOv6, và YOLOv7.
- Kết quả cung cấp như sau:

| Metric | CNN | YOLOv5s | YOLOv5m | YOLOv5 (no pretrained weights) | YOLOv6 | YOLOv7 |
|---|---:|---:|---:|---:|---:|---:|
| Task | Image Classification | Object Detection | Object Detection | Object Detection | Object Detection | Object Detection |
| Accuracy | 99.22% | unknown | unknown | unknown | unknown | unknown |
| Precision | unknown | 0.885 | 0.936 | 0.679 | unknown | 0.554 |
| Recall | unknown | 0.985 | 0.955 | 0.970 | unknown | 1.000 |
| mAP@0.5 | unknown | 0.972 | 0.981 | 0.853 | 0.644* | 0.737 |
| mAP@0.5:0.95 | unknown | 0.832 | 0.861 | 0.642 | 0.548* | 0.608 |
| Inference Speed | unknown | 12.3 ms | 21.9 ms | 22.0 ms | 16.0 ms | 42.7 ms |