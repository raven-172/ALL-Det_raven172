[KDownloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 14.8MB/s 0.4s3s<0.5s.4s0s
YOLOv8n summary: 129 layers, 3,157,200 parameters, 0 gradients, 8.9 GFLOPs
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
[34m[1mengine\trainer: [0magnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, channels_last=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, cls_remap=True, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dgrad=0.5, dis=6.0, distill_model=None, dlam=1.0, dlog=1.0, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, iou=0.7, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=YOLOv8-results, nbs=64, nms=None, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results, quantize=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=42, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=tracktrack.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=0, workspace=None
Overriding model.yaml nc=80 with nc=1

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 
 22        [15, 18, 21]  1    751507  ultralytics.nn.modules.head.Detect           [1, 16, None, [64, 128, 256]] 
Model summary: 129 layers, 3,011,043 parameters, 3,011,027 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
[34m[1mAMP: [0mrunning Automatic Mixed Precision (AMP) checks...
[34m[1mAMP: [0mdownloading yolo26n.pt for AMP checks (one-time, not used for training)...
[KDownloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt to 'C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\weights\yolo26n.pt': 100% ━━━━━━━━━━━━ 5.3MB 11.3MB/s 0.5s.4s<0.1s4s2s
[34m[1mAMP: [0mchecks passed 
[34m[1mtrain: [0mFast image access  (ping: 0.00.0 ms, read: 2419.0230.8 MB/s, size: 1173.3 KB)
[K[34m[1mtrain: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\train.cache... 91 images, 49 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 91/91  0.0s
[34m[1mval: [0mFast image access  (ping: 0.00.0 ms, read: 2640.4240.8 MB/s, size: 1271.6 KB)
[K[34m[1mval: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\val.cache... 16 images, 9 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 16/16  0.0s
[34m[1moptimizer:[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and determining best 'optimizer' and 'lr0' automatically... 
[34m[1moptimizer:[0m AdamW(lr=0.002, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results\labels.jpg... 
Using 91 train, 16 val images for fraction=1.0 at imgsz=640
Using 0 dataloader workers
Logging results to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results[0m
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      1/100      1.18G      1.287      3.734       1.21         17        640: 100% ━━━━━━━━━━━━ 12/12 3.5it/s 3.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127    0.00729      0.276    0.00456    0.00217

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      2/100      1.29G      1.223      2.304     0.9688         36        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127     0.0265          1     0.0456     0.0287

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      3/100      1.29G      1.146      1.766      1.005         33        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.025      0.945     0.0343     0.0217

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      4/100      1.29G      1.361      3.113      1.105         23        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0258      0.976     0.0362     0.0234

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      5/100      1.29G      1.426      2.057      1.128         14        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127     0.0219      0.827     0.0207     0.0123

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      6/100      1.29G     0.9763      1.524     0.9798          9        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.024      0.906     0.0551     0.0389

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      7/100      1.29G     0.9016      1.399      0.992          5        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.921      0.368      0.854      0.693

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      8/100      1.29G     0.7874      1.296     0.9288         24        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.845      0.661      0.871      0.683

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      9/100      1.29G     0.7891      1.119     0.9483         12        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.799      0.848      0.893       0.71

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     10/100      1.29G     0.8158      1.908     0.9941         23        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.829      0.802      0.901      0.731

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     11/100      1.29G     0.7935      1.153     0.9032          8        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127       0.83      0.844      0.912      0.737

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     12/100       1.3G     0.7512     0.9331     0.9173         12        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.826      0.937      0.937      0.773

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     13/100       1.3G     0.7469     0.9781      0.901         25        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.813      0.787      0.895      0.761

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     14/100       1.3G     0.6969     0.8638     0.8858         21        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.825      0.819      0.899       0.76

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     15/100       1.3G     0.9416      1.855      1.023          1        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.888      0.835      0.933      0.798

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     16/100       1.3G     0.6933       1.14     0.8769         28        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.864      0.904      0.944      0.809

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     17/100       1.3G     0.6777     0.8668     0.8886         16        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.784      0.953      0.923      0.807

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     18/100       1.3G     0.6144      1.053     0.8804         41        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.849      0.882      0.923      0.807

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     19/100       1.3G      0.673      1.036     0.8819         14        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127       0.83      0.959      0.952      0.788

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     20/100       1.3G     0.7248      1.006     0.8688         32        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.836      0.937      0.944      0.793

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     21/100       1.3G     0.7086     0.8155     0.8807         63        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.823      0.953      0.923      0.812

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     22/100       1.3G     0.6291     0.9734     0.8572          5        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.835      0.953      0.939      0.813

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     23/100       1.3G     0.6532     0.8586     0.8723         27        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.862      0.969      0.944      0.814

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     24/100       1.3G     0.6378     0.8313      0.887         16        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.877       0.95       0.93      0.823

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     25/100       1.3G     0.6202     0.7984     0.8685         28        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.839      0.941      0.914      0.799

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     26/100       1.3G     0.6694     0.7589     0.8547         32        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.763      0.913      0.876      0.767

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     27/100       1.3G     0.5927      1.081     0.8899          4        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.882      0.976      0.953      0.834

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     28/100       1.3G     0.5988      0.912     0.8641          8        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.878      0.921      0.942      0.817

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     29/100       1.3G     0.5649     0.8197     0.8724         15        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.864      0.948      0.952      0.843

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     30/100       1.3G       0.58     0.7247      0.864          9        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.887      0.969      0.955      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     31/100       1.3G     0.6007      0.804     0.8572         34        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.885      0.971      0.953      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     32/100       1.3G     0.5682     0.8168     0.8598          2        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.866      0.976      0.954      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     33/100       1.3G     0.5956     0.7161     0.8676         19        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.89      0.956      0.946      0.841

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     34/100       1.3G     0.5461     0.7705      0.841         11        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.919      0.906      0.945      0.839

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     35/100       1.3G     0.5475     0.7894     0.8471         14        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127      0.907      0.945      0.954       0.84

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     36/100       1.3G     0.5778     0.6912     0.8603          8        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.895      0.992      0.961       0.85

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     37/100       1.3G     0.5591     0.7404     0.8485         29        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.867      0.969      0.954      0.853

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     38/100       1.3G      0.557     0.6277     0.8523          9        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.874      0.969      0.951      0.858

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     39/100       1.3G     0.5772     0.6369     0.8683         19        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.87      0.984       0.96      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     40/100       1.3G     0.5575      0.573     0.8491         34        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.907      0.937      0.964       0.86

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     41/100       1.3G     0.5408      0.804     0.8357          1        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.864      0.921      0.939      0.832

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     42/100       1.3G     0.5673     0.5987     0.8598         18        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.888      0.913      0.943       0.83

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     43/100       1.3G      0.538     0.6065     0.8405         44        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.904      0.953      0.951      0.849

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     44/100       1.3G     0.5967     0.6191     0.8553         17        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.867      0.975      0.949      0.848

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     45/100       1.3G     0.5688     0.6077      0.845         23        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.916      0.939      0.951      0.857

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     46/100       1.3G     0.5164     0.6011     0.8674         21        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.889      0.969      0.955      0.853

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     47/100       1.3G     0.5794     0.5997     0.8551         12        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.898      0.973      0.955      0.857

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     48/100       1.3G     0.5252     0.5895     0.8444          3        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.886      0.976      0.956      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     49/100       1.3G     0.5308     0.5984     0.8691         17        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.868      0.982      0.954      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     50/100       1.3G     0.5222     0.5617     0.8337          8        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127       0.86      0.976      0.956      0.854

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     51/100       1.3G     0.5534     0.5598     0.8652         15        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127       0.88      0.978      0.957      0.863

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     52/100       1.3G     0.5041     0.5357     0.8493          9        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.893      0.981      0.958      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     53/100       1.3G     0.4942     0.5055     0.8242         16        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.871      0.976      0.959      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     54/100       1.3G     0.5491     0.5766     0.8691         13        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.871      0.992       0.96      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     55/100       1.3G     0.4998     0.5114       0.83         10        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.919      0.986      0.965      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     56/100       1.3G     0.4995     0.5533     0.8286         24        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.913      0.992      0.963      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     57/100       1.3G     0.4724     0.5238     0.8346         16        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.913      0.989       0.96      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     58/100       1.3G      0.523     0.5265     0.8217         11        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.909          1      0.958      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     59/100       1.3G      0.524     0.4946     0.8399         15        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.897          1      0.963      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     60/100       1.3G     0.5005     0.5727     0.8376          9        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.894      0.995      0.965      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     61/100       1.3G     0.5123     0.5079     0.8253         53        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.906      0.985      0.969      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     62/100       1.3G     0.4984     0.5114     0.8461         20        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.904      0.984      0.968      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     63/100       1.3G     0.5208     0.4742       0.84         12        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.875      0.992      0.958      0.855

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     64/100       1.3G     0.5127     0.4978     0.8478         32        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.874      0.984      0.954      0.848

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     65/100       1.3G      0.492     0.4885     0.8263         17        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.877      0.984       0.95      0.852

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     66/100       1.3G     0.5216     0.5098     0.8356          7        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.892      0.974      0.951      0.846

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     67/100       1.3G     0.4467     0.4874     0.8302         21        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.875      0.992       0.95       0.85

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     68/100       1.3G     0.4744     0.4569      0.847         10        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.882      0.997       0.95       0.85

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     69/100       1.3G     0.4509     0.4769      0.824         29        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127        0.9      0.976      0.952      0.861

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     70/100       1.3G     0.4608     0.4887     0.8465         24        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.893       0.99      0.955      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     71/100       1.3G     0.5014     0.4416      0.822         11        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.922      0.937      0.955      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     72/100       1.3G     0.4682      0.462     0.8435         39        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.909      0.941      0.956      0.872

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     73/100       1.3G     0.5055     0.4548     0.8242         45        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.92      0.945      0.961      0.875

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     74/100       1.3G     0.4849     0.4721     0.8399         32        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.974      0.963      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     75/100       1.3G     0.4658     0.4494     0.8198         10        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.966      0.962      0.875

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     76/100       1.3G      0.454     0.4439     0.8237         11        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.965      0.961      0.875

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     77/100       1.3G     0.4895     0.4801     0.8089          6        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.917      0.953       0.96      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     78/100       1.3G     0.5634     0.9508     0.8398          1        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.91      0.953      0.957      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     79/100       1.3G     0.4475     0.4873      0.838         10        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.91      0.969      0.957      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     80/100       1.3G      0.463     0.4337     0.8211          8        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.912      0.984       0.96      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     81/100       1.3G     0.4721     0.4234     0.8235         11        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.918      0.976      0.964      0.884

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     82/100       1.3G     0.4485     0.3986     0.8151         13        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.913      0.987      0.965      0.879

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     83/100       1.3G     0.4767       0.44     0.8248         34        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.926      0.981      0.966      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     84/100       1.3G     0.4711     0.4329     0.8263         30        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.919      0.988      0.966      0.883

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     85/100       1.3G     0.4403     0.4242     0.8329         35        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.923      0.969      0.967      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     86/100       1.3G     0.4622     0.4306     0.8228         32        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.939      0.953      0.967       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     87/100       1.3G     0.4301     0.4566     0.8346         20        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.912      0.981      0.964       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     88/100       1.3G     0.4665     0.4499     0.8309         42        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.912      0.982      0.964      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     89/100       1.3G     0.4625     0.4527     0.8265          5        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.928      0.961      0.965      0.866

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     90/100       1.3G     0.4135      0.408     0.8172         13        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.939      0.976      0.966       0.87
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     91/100       1.3G     0.3636     0.7986     0.7603          0        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.925      0.992      0.968      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     92/100       1.3G     0.4006     0.4682     0.8198          6        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.913          1      0.968      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     93/100       1.3G     0.4103     0.4538     0.8019          1        640: 100% ━━━━━━━━━━━━ 12/12 5.7it/s 2.1s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.922      0.984       0.97       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     94/100       1.3G     0.3925     0.4999     0.8007         28        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.984       0.97      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     95/100       1.3G     0.4213     0.4386     0.8072          3        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.934      0.976       0.97      0.883

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     96/100       1.3G      0.398     0.4025     0.8003         22        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.929      0.984       0.97       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     97/100       1.3G     0.4487     0.4274     0.8348         15        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.934      0.998      0.969       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     98/100       1.3G     0.4335     0.4179     0.8125         19        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.933          1      0.969      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     99/100       1.3G     0.4014      1.303     0.7472         16        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.933          1      0.968      0.884

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K    100/100       1.3G      0.407     0.3941     0.8099          8        640: 100% ━━━━━━━━━━━━ 12/12 5.5it/s 2.2s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.931          1      0.968      0.883

100 epochs completed in 0.087 hours.
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results\weights\last.pt, 6.2MB
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results\weights\best.pt, 6.2MB

Validating C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results\weights\best.pt...
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
Model summary (fused): 72 layers, 3,005,843 parameters, 0 gradients, 8.1 GFLOPs
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.922      0.976      0.966      0.888
Speed: 0.1ms preprocess, 1.3ms inference, 0.0ms loss, 1.0ms postprocess per image
Results saved to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results[0m
Training results: C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv8-results\YOLOv8-results