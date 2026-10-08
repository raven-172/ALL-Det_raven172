[KDownloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo11n.pt to 'yolo11n.pt': 100% ━━━━━━━━━━━━ 5.4MB 14.0MB/s 0.4s.3s<0.2s.0s
YOLO11n summary: 181 layers, 2,624,080 parameters, 0 gradients, 6.7 GFLOPs
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
[34m[1mengine\trainer: [0magnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, channels_last=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, cls_remap=True, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dgrad=0.5, dis=6.0, distill_model=None, dlam=1.0, dlog=1.0, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, iou=0.7, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolo11n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=YOLO11-result, nbs=64, nms=None, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results, quantize=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=42, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=tracktrack.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=0, workspace=None
Overriding model.yaml nc=80 with nc=1

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      6640  ultralytics.nn.modules.block.C3k2            [32, 64, 1, False, 0.25]      
  3                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
  4                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     
  5                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
  6                  -1  1     87040  ultralytics.nn.modules.block.C3k2            [128, 128, 1, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    111296  ultralytics.nn.modules.block.C3k2            [384, 128, 1, False]          
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1     32096  ultralytics.nn.modules.block.C3k2            [256, 64, 1, False]           
 17                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1     86720  ultralytics.nn.modules.block.C3k2            [192, 128, 1, False]          
 20                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1    378880  ultralytics.nn.modules.block.C3k2            [384, 256, 1, True]           
 23        [16, 19, 22]  1    430867  ultralytics.nn.modules.head.Detect           [1, 16, None, [64, 128, 256]] 
YOLO11n summary: 181 layers, 2,590,035 parameters, 2,590,019 gradients, 6.5 GFLOPs

Transferred 448/499 items from pretrained weights
Freezing layer 'model.23.dfl.conv.weight'
[34m[1mAMP: [0mrunning Automatic Mixed Precision (AMP) checks...
[34m[1mAMP: [0mchecks passed 
[34m[1mtrain: [0mFast image access  (ping: 0.00.0 ms, read: 2143.2287.5 MB/s, size: 1173.3 KB)
[K[34m[1mtrain: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\train.cache... 91 images, 49 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 91/91  0.0s
[34m[1mval: [0mFast image access  (ping: 0.00.0 ms, read: 1966.0349.3 MB/s, size: 1271.6 KB)
[K[34m[1mval: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\val.cache... 16 images, 9 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 16/16  0.0s
[34m[1moptimizer:[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and determining best 'optimizer' and 'lr0' automatically... 
[34m[1moptimizer:[0m AdamW(lr=0.002, momentum=0.9) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
Plotting labels to C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result\labels.jpg... 
Using 91 train, 16 val images for fraction=1.0 at imgsz=640
Using 0 dataloader workers
Logging results to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result[0m
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      1/100      1.27G       1.21       3.37      1.127         17        640: 100% ━━━━━━━━━━━━ 12/12 1.5it/s 7.9s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 1.1s/it 1.1s
                   all         16        127     0.0265          1     0.0615     0.0416

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      2/100      1.47G      1.153       2.08     0.9999         36        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127     0.0206       0.78     0.0237    0.00701

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      3/100      1.47G      1.102      1.757     0.9785         33        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0265          1     0.0394     0.0229

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      4/100      1.47G      1.101      1.818     0.9587         23        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0254      0.961     0.0301     0.0188

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      5/100      1.47G     0.9892      1.514     0.9665         14        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127     0.0223      0.843      0.286      0.205

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      6/100      1.47G     0.9216      1.414     0.9436          9        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.034      0.953      0.587      0.445

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      7/100      1.47G     0.9118       1.43     0.9672          5        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127     0.0242      0.913     0.0511     0.0399

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      8/100      1.47G     0.7601      1.423     0.9108         24        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.119      0.333      0.149      0.121

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      9/100      1.47G      0.781      1.223     0.9336         12        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.813      0.866      0.885      0.727

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     10/100      1.47G     0.7611      1.965     0.9592         23        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.855      0.835      0.902      0.767

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     11/100      1.47G     0.7693      1.243     0.8913          8        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127      0.809      0.937      0.912      0.788

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     12/100      1.47G     0.7102     0.9287     0.8983         12        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.776      0.982      0.893       0.75

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     13/100      1.47G     0.7529      1.099     0.8885         25        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.767      0.953        0.9      0.764

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     14/100      1.47G     0.6924     0.9294     0.8792         21        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.785      0.945      0.917      0.783

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     15/100      1.47G     0.8688      2.915     0.9549          1        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.829      0.953      0.933      0.796

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     16/100      1.47G     0.6967     0.8649     0.8695         28        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.823      0.961      0.933      0.791

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     17/100      1.47G     0.6463     0.8777     0.8689         16        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.862      0.921      0.948      0.816

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     18/100      1.47G     0.6134      1.023     0.8661         41        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.834      0.969      0.939      0.815

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     19/100      1.47G     0.6336      1.062     0.8662         14        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.855      0.925      0.967      0.797

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     20/100      1.47G     0.6992     0.8672     0.8598         32        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.844      0.937       0.96      0.803

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     21/100      1.47G     0.7333     0.8171      0.879         63        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.863      0.913      0.957      0.815

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     22/100      1.47G     0.6629      0.954     0.8591          5        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.827      0.992      0.958      0.828

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     23/100      1.47G      0.687     0.8858     0.8699         27        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.805      0.945      0.931      0.794

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     24/100      1.47G     0.6572     0.7958     0.8908         16        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.832      0.961      0.948      0.833

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     25/100      1.47G     0.6353     0.8032     0.8631         28        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.915      0.935      0.958      0.831

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     26/100      1.47G     0.6564     0.7792     0.8538         32        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.906      0.937      0.957      0.842

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     27/100      1.47G     0.6013     0.9812      0.883          4        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.853      0.945      0.957      0.836

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     28/100      1.47G     0.6358      1.018     0.8642          8        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.808      0.961      0.947      0.802

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     29/100      1.47G     0.6033     0.8556     0.8811         15        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.845      0.961      0.959      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     30/100      1.47G     0.5735     0.7679     0.8547          9        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.882      0.945      0.964      0.846

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     31/100      1.47G     0.6016     0.8101     0.8548         34        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.869      0.937      0.964      0.844

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     32/100      1.47G     0.6155     0.8681     0.8626          2        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.872      0.929       0.96      0.844

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     33/100      1.47G     0.6104     0.7808      0.866         19        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.891      0.953      0.966      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     34/100      1.47G     0.5804     0.8645     0.8429         11        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.888      0.936      0.955      0.845

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     35/100      1.47G     0.5531     0.8628     0.8481         14        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.861      0.975       0.96      0.834

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     36/100      1.47G      0.606     0.7687     0.8624          8        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.889      0.953      0.967      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     37/100      1.47G     0.5645     0.7782     0.8469         29        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.851      0.976      0.961       0.84

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     38/100      1.47G     0.5873     0.6395      0.853          9        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.876      0.942      0.962      0.855

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     39/100      1.47G     0.5791     0.6639     0.8567         19        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.912      0.976      0.969      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     40/100      1.47G     0.5542     0.6333     0.8469         34        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.932      0.977      0.973      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     41/100      1.47G     0.5539      0.852     0.8339          1        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.915      0.969      0.977      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     42/100      1.47G     0.5574     0.6172     0.8594         18        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.885      0.984      0.972      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     43/100      1.47G     0.5411     0.6448     0.8393         44        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.881      0.945      0.958      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     44/100      1.47G     0.5972     0.6625     0.8545         17        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.876      0.929       0.95      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     45/100      1.47G     0.5605     0.6381     0.8501         23        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.894      0.945      0.959      0.849

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     46/100      1.47G     0.5493     0.6632     0.8692         21        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.884      0.961      0.958      0.848

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     47/100      1.47G     0.5822     0.6428      0.852         12        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.907      0.961      0.955      0.851

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     48/100      1.47G     0.5259     0.6558     0.8402          3        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.93      0.939       0.96      0.861

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     49/100      1.47G     0.5438     0.6866     0.8657         17        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.914      0.976      0.975      0.869

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     50/100      1.47G     0.5269     0.6088     0.8309          8        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.894      0.984      0.977      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     51/100      1.47G      0.552     0.6163     0.8565         15        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.893      0.989      0.971      0.859

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     52/100      1.47G     0.5245     0.5974     0.8475          9        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.91      0.954      0.969      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     53/100      1.47G     0.5263     0.5598     0.8271         16        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.91      0.959      0.962      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     54/100      1.47G       0.54     0.6573     0.8643         13        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.879      0.984      0.965      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     55/100      1.47G     0.5141     0.5598     0.8291         10        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.911      0.961      0.968      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     56/100      1.47G     0.5072     0.6263     0.8251         24        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.912      0.969      0.968      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     57/100      1.47G     0.4844     0.5753     0.8363         16        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.911       0.97      0.971       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     58/100      1.47G     0.5363     0.5938     0.8209         11        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.904      0.976      0.968      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     59/100      1.47G     0.5335     0.5449     0.8384         15        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.891      0.969      0.964       0.86

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     60/100      1.47G      0.524     0.6667     0.8428          9        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.892      0.973      0.969      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     61/100      1.47G     0.5188     0.5623      0.819         53        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.91      0.955      0.968      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     62/100      1.47G     0.5067     0.5494     0.8439         20        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.91      0.955      0.966       0.87

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     63/100      1.47G     0.5209       0.52     0.8373         12        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.903      0.953      0.969      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     64/100      1.47G     0.5032     0.5351     0.8394         32        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.916      0.948      0.969      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     65/100      1.47G     0.4945     0.5131     0.8212         17        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.909      0.969      0.968      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     66/100      1.47G      0.537     0.5532     0.8347          7        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.902      0.969      0.968      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     67/100      1.47G     0.4455     0.5176     0.8288         21        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.91      0.959      0.969      0.879

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     68/100      1.47G     0.4712     0.5031     0.8438         10        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.923      0.948      0.966      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     69/100      1.47G     0.4614     0.5314     0.8246         29        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.867      0.979      0.962      0.869

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     70/100      1.47G     0.4816     0.5342     0.8497         24        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.896      0.952      0.963      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     71/100      1.47G     0.5135     0.4939     0.8236         11        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.937      0.961      0.969      0.871

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     72/100      1.47G     0.4771     0.5004     0.8418         39        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.938      0.961      0.968      0.879

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     73/100      1.47G     0.5094     0.4935     0.8237         45        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.928      0.961      0.974       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     74/100      1.47G     0.4989     0.5136      0.839         32        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.931      0.962      0.977       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     75/100      1.47G      0.484     0.5091     0.8243         10        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.939      0.972      0.978      0.869

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     76/100      1.47G     0.4744     0.4836     0.8227         11        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.946      0.972      0.978      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     77/100      1.47G     0.5078     0.5184     0.8105          6        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.933      0.979      0.977      0.892

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     78/100      1.47G     0.5557      1.032     0.8325          1        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.931      0.984      0.977      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     79/100      1.47G     0.4772     0.5457     0.8383         10        640: 100% ━━━━━━━━━━━━ 12/12 5.6it/s 2.1s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.936      0.961      0.972      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     80/100      1.47G     0.4833     0.4929     0.8217          8        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.933      0.945      0.971      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     81/100      1.47G     0.4815     0.4952     0.8215         11        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.934      0.969      0.977      0.889

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     82/100      1.47G     0.4576     0.4404     0.8134         13        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.939      0.976      0.976      0.888

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     83/100      1.47G     0.4994     0.4934     0.8242         34        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.929      0.976      0.971      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     84/100      1.47G     0.4908      0.492     0.8335         30        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.937      0.976      0.973      0.883

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     85/100      1.47G      0.458     0.4668     0.8326         35        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.946      0.964      0.976      0.894

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     86/100      1.47G     0.4844     0.5028      0.825         32        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.945      0.947      0.974      0.886

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     87/100      1.47G     0.4563     0.5505     0.8378         20        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.924      0.961      0.972      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     88/100      1.47G     0.4995     0.4982     0.8343         42        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.929      0.961      0.973      0.885

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     89/100      1.47G     0.4764       0.49     0.8278          5        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.938      0.958      0.976      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     90/100      1.47G     0.4374      0.455     0.8182         13        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.936      0.961      0.976      0.881
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     91/100      1.47G     0.3693      1.257     0.7562          0        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.926      0.961      0.979      0.886

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     92/100      1.47G     0.4104     0.5323     0.8141          6        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.934      0.953       0.98      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     93/100      1.47G     0.4266     0.5247     0.8027          1        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.936      0.961      0.982      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     94/100      1.47G     0.3911     0.5768     0.7968         28        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.932       0.97      0.983      0.889

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     95/100      1.47G     0.4379      0.487     0.8077          3        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.927      0.992      0.983      0.886

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     96/100      1.47G     0.4162     0.4392      0.803         22        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.931      0.992      0.981      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     97/100      1.47G     0.4652     0.4865     0.8337         15        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.931      0.992       0.98      0.888

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     98/100      1.47G     0.4604     0.4618     0.8148         19        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.933       0.99       0.98      0.891

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     99/100      1.47G     0.4182      1.788     0.7451         16        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127       0.95      0.969      0.982      0.887

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K    100/100      1.47G     0.4297     0.4466     0.8133          8        640: 100% ━━━━━━━━━━━━ 12/12 5.5it/s 2.2s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.949      0.969      0.982      0.888

100 epochs completed in 0.092 hours.
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result\weights\last.pt, 5.5MB
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result\weights\best.pt, 5.5MB

Validating C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result\weights\best.pt...
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
YOLO11n summary (fused): 100 layers, 2,582,347 parameters, 0 gradients, 6.4 GFLOPs
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.946      0.963      0.976      0.885
Speed: 0.2ms preprocess, 1.5ms inference, 0.0ms loss, 1.1ms postprocess per image
Results saved to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result[0m
Training results: C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO11-results\YOLO11-result