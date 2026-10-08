YOLOv5n summary: 153 layers, 2,654,816 parameters, 0 gradients, 7.8 GFLOPs
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
[34m[1mengine\trainer: [0magnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, channels_last=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, cls_remap=True, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dgrad=0.5, dis=6.0, distill_model=None, dlam=1.0, dlog=1.0, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, iou=0.7, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov5nu.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=YOLOv5nu-results-3, nbs=64, nms=None, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results, quantize=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=42, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=tracktrack.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=0, workspace=None
[KDownloading https://ultralytics.com/assets/Arial.ttf to 'C:\Users\ezycloudx-admin\AppData\Roaming\Ultralytics\Arial.ttf': 100% ━━━━━━━━━━━━ 755.1KB 3.7MB/s 0.2s 0.1s<0.5s
Overriding model.yaml nc=80 with nc=1

                   from  n    params  module                                       arguments                     
  0                  -1  1      1760  ultralytics.nn.modules.conv.Conv             [3, 16, 6, 2, 2]              
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      4800  ultralytics.nn.modules.block.C3              [32, 32, 1]                   
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     29184  ultralytics.nn.modules.block.C3              [64, 64, 2]                   
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  3    156928  ultralytics.nn.modules.block.C3              [128, 128, 3]                 
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    296448  ultralytics.nn.modules.block.C3              [256, 256, 1]                 
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1     33024  ultralytics.nn.modules.conv.Conv             [256, 128, 1, 1]              
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1     90880  ultralytics.nn.modules.block.C3              [256, 128, 1, False]          
 14                  -1  1      8320  ultralytics.nn.modules.conv.Conv             [128, 64, 1, 1]               
 15                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 16             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 17                  -1  1     22912  ultralytics.nn.modules.block.C3              [128, 64, 1, False]           
 18                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 19            [-1, 14]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 20                  -1  1     74496  ultralytics.nn.modules.block.C3              [128, 128, 1, False]          
 21                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 22            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 23                  -1  1    296448  ultralytics.nn.modules.block.C3              [256, 256, 1, False]          
 24        [17, 20, 23]  1    751507  ultralytics.nn.modules.head.Detect           [1, 16, None, [64, 128, 256]] 
YOLOv5n summary: 153 layers, 2,508,659 parameters, 2,508,643 gradients, 7.2 GFLOPs

Transferred 391/427 items from pretrained weights
Freezing layer 'model.24.dfl.conv.weight'
[34m[1mAMP: [0mrunning Automatic Mixed Precision (AMP) checks...
[34m[1mAMP: [0mdownloading yolo26n.pt for AMP checks (one-time, not used for training)...
[KDownloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt to 'C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\weights\yolo26n.pt': 100% ━━━━━━━━━━━━ 5.3MB 13.7MB/s 0.4s.3s<0.3s.1ss
[34m[1mAMP: [0mchecks passed 
[34m[1mtrain: [0mFast image access  (ping: 0.00.0 ms, read: 256.3152.8 MB/s, size: 1173.3 KB)
[K[34m[1mtrain: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\train... 91 images, 49 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 91/91 1.0Kit/s 0.1s
[34m[1mtrain: [0mNew cache created: C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\train.cache
[34m[1mval: [0mFast image access  (ping: 0.00.0 ms, read: 290.5146.7 MB/s, size: 1271.6 KB)
[K[34m[1mval: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\val... 16 images, 9 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 16/16 1.9Kit/s 0.0s
[34m[1mval: [0mNew cache created: C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\val.cache
[34m[1moptimizer:[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and determining best 'optimizer' and 'lr0' automatically... 
[34m[1moptimizer:[0m AdamW(lr=0.002, momentum=0.9) with parameter groups 69 weight(decay=0.0), 76 weight(decay=0.0005), 75 bias(decay=0.0)
Plotting labels to C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3\labels.jpg... 
Using 91 train, 16 val images for fraction=1.0 at imgsz=640
Using 0 dataloader workers
Logging results to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3[0m
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      1/100      1.15G      1.199      3.763       1.17         17        640: 100% ━━━━━━━━━━━━ 12/12 2.8it/s 4.3s0.3s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.0it/s 0.5s
                   all         16        127     0.0177      0.669     0.0287     0.0166

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      2/100      1.23G      1.069      2.435     0.9116         36        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0265          1      0.067     0.0408

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      3/100      1.23G       1.09       1.81     0.9567         33        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127     0.0265          1      0.297      0.215

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      4/100      1.23G      1.008      1.973     0.9393         23        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127     0.0227      0.858      0.233      0.175

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      5/100      1.23G      1.133      1.611     0.9978         14        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.808      0.567      0.791      0.599

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      6/100      1.23G     0.8426      1.552      0.906          9        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.703      0.579      0.704      0.542

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      7/100      1.23G     0.8923      1.519     0.9365          5        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.74      0.876      0.815      0.656

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      8/100      1.23G     0.7747      1.461     0.9069         24        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.78      0.867      0.832      0.662

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K      9/100      1.23G     0.7912      1.344     0.9231         12        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.765      0.898      0.881      0.706

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     10/100      1.23G      0.791      2.068     0.9482         23        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.772       0.89      0.874      0.736

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     11/100      1.23G     0.8095      1.217     0.8914          8        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.777      0.898       0.89      0.749

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     12/100      1.23G       0.77      1.022     0.9023         12        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.811      0.913      0.906      0.761

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     13/100      1.23G     0.7626      1.087     0.8751         25        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.856      0.921      0.913      0.786

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     14/100      1.23G     0.7214     0.9698     0.8769         21        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.874      0.898      0.938      0.786

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     15/100      1.23G     0.8614      1.964     0.9664          1        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.851      0.772      0.928      0.774

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     16/100      1.23G     0.7581      1.158      0.875         28        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.849      0.839      0.924      0.767

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     17/100      1.23G     0.6693     0.9555     0.8633         16        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.824      0.882      0.909      0.767

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     18/100      1.23G     0.6309      1.111     0.8634         41        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.77      0.952      0.891      0.769

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     19/100      1.23G     0.6994      1.143     0.8572         14        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.733      0.887       0.87      0.713

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     20/100      1.23G     0.7066      1.081     0.8539         32        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.805      0.945      0.906      0.745

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     21/100      1.23G     0.7094     0.9441     0.8706         63        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.862      0.945      0.929      0.814

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     22/100      1.23G     0.6359      1.102     0.8522          5        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.853      0.959      0.932      0.816

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     23/100      1.23G     0.6461     0.8847     0.8465         27        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.845      0.945      0.941       0.83

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     24/100      1.23G     0.6519     0.8791     0.8791         16        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.847      0.961      0.942       0.82

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     25/100      1.23G     0.6566     0.8788     0.8601         28        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.841      0.961      0.933      0.806

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     26/100      1.23G     0.6662     0.8075     0.8461         32        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.848      0.965      0.932      0.813

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     27/100      1.23G     0.6132      1.112     0.8664          4        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.84       0.99      0.952      0.833

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     28/100      1.23G      0.621      1.009     0.8531          8        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.906      0.945      0.957      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     29/100      1.23G     0.6142     0.9135     0.8615         15        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.908      0.898      0.957      0.849

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     30/100      1.23G     0.5896     0.7769     0.8514          9        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.858      0.997      0.963      0.852

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     31/100      1.23G     0.6167     0.8533     0.8528         34        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.834      0.992       0.95      0.844

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     32/100      1.23G     0.5933     0.8267     0.8494          2        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.84      0.995      0.948      0.839

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     33/100      1.23G     0.6416       0.81     0.8608         19        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.826      0.984      0.951      0.834

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     34/100      1.23G     0.5824     0.8998     0.8472         11        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.826      0.973      0.953      0.835

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     35/100      1.23G      0.575     0.8267     0.8467         14        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.874       0.93      0.958      0.854

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     36/100      1.23G     0.5917     0.7759     0.8591          8        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.0it/s 0.5s
                   all         16        127      0.855      0.976      0.959       0.85

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     37/100      1.23G     0.5951     0.8351     0.8471         29        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.873      0.921      0.955      0.852

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     38/100      1.23G     0.5759     0.6948      0.846          9        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.868      0.929      0.951      0.857

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     39/100      1.23G     0.5916      0.696     0.8626         19        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.888      0.953       0.96      0.856

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     40/100      1.23G     0.5745     0.6588     0.8504         34        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.887      0.969      0.965      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     41/100      1.23G     0.5583     0.8914     0.8288          1        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.849      0.992      0.961      0.866

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     42/100      1.23G     0.5781     0.6541      0.866         18        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.907      0.927      0.958      0.858

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     43/100      1.23G     0.5912     0.7063     0.8458         44        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.877      0.953      0.963      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     44/100      1.23G     0.6131     0.7048     0.8525         17        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.888      0.934      0.959      0.855

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     45/100      1.23G     0.5772     0.6665     0.8467         23        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.854      0.965      0.957      0.846

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     46/100      1.23G      0.554     0.7115     0.8593         21        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.851      0.945       0.95      0.816

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     47/100      1.23G     0.5874      0.669     0.8407         12        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.825      0.953      0.939      0.834

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     48/100      1.23G     0.5448     0.6727     0.8399          3        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.83      0.996      0.951      0.847

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     49/100      1.23G      0.538     0.6598      0.856         17        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.913      0.937      0.969      0.861

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     50/100      1.23G     0.5513     0.6195     0.8293          8        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.923      0.953      0.971      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     51/100      1.23G     0.5571     0.6276     0.8505         15        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.923      0.961      0.974      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     52/100      1.23G     0.5474     0.5944     0.8486          9        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.918       0.97      0.973      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     53/100      1.23G     0.5127     0.5431     0.8219         16        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.899       0.98       0.97      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     54/100      1.23G     0.5695     0.6412     0.8689         13        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127        0.9      0.993      0.971       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     55/100      1.23G     0.5243     0.5755     0.8266         10        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.91      0.992      0.973       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     56/100      1.23G     0.5183     0.6423     0.8263         24        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.904      0.984      0.971      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     57/100      1.23G     0.5006     0.6214      0.829         16        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.924      0.961      0.971      0.875

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     58/100      1.23G     0.5288     0.6038     0.8141         11        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.895      0.969      0.966      0.865

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     59/100      1.23G     0.5707     0.5924     0.8423         15        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.885      0.967      0.964      0.864

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     60/100      1.23G     0.5276     0.6645     0.8436          9        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.894      0.961      0.969      0.859

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     61/100      1.23G     0.5405     0.5751     0.8237         53        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.885      0.969       0.97      0.844

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     62/100      1.23G     0.5106     0.5723     0.8369         20        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.885      0.969       0.97      0.858

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     63/100      1.23G     0.5315     0.5525     0.8347         12        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.909      0.953      0.973       0.87

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     64/100      1.23G     0.5256     0.5734     0.8376         32        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.895      0.953       0.97      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     65/100      1.23G      0.506     0.5415     0.8243         17        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.921      0.918      0.967      0.872

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     66/100      1.23G     0.5466      0.574     0.8298          7        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.91      0.945      0.967       0.87

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     67/100      1.23G     0.4536      0.532     0.8254         21        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.879      0.984      0.968      0.862

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     68/100      1.23G     0.4815     0.5263     0.8401         10        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127        0.9      0.989      0.971      0.866

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     69/100      1.23G     0.4803     0.5408     0.8227         29        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.91       0.96      0.974      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     70/100      1.23G     0.4897     0.5522     0.8437         24        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.91      0.955      0.971      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     71/100      1.23G      0.518     0.5182     0.8259         11        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.906      0.969      0.975      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     72/100      1.23G     0.4806     0.5393     0.8411         39        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.917      0.984      0.979      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     73/100      1.23G      0.524     0.5085     0.8249         45        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.928      0.984       0.98      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     74/100      1.23G     0.5017     0.5348     0.8306         32        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.933      0.984       0.98       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     75/100      1.23G     0.4878     0.5197     0.8224         10        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.932      0.992       0.98       0.89

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     76/100      1.23G     0.4596     0.4818     0.8173         11        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.94      0.991      0.979      0.888

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     77/100      1.23G     0.5237     0.5256     0.8075          6        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.94      0.991       0.98       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     78/100      1.23G     0.5476     0.8767      0.837          1        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.94      0.986      0.979      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     79/100      1.23G      0.485     0.5252      0.829         10        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.933      0.992      0.979      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     80/100      1.23G     0.4783     0.4817     0.8157          8        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.932      0.992      0.979      0.876

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     81/100      1.23G     0.4835     0.4938     0.8152         11        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.913      0.976      0.978      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     82/100      1.23G     0.4676     0.4563     0.8125         13        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.911      0.969      0.978      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     83/100      1.23G     0.5065      0.482     0.8253         34        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.5s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.944      0.936      0.977      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     84/100      1.23G     0.4938     0.4778     0.8279         30        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.925      0.974      0.976      0.878

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     85/100      1.23G     0.4815     0.4744     0.8312         35        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.933      0.981      0.977      0.881

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     86/100      1.23G     0.5055     0.4778     0.8285         32        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.932      0.984      0.975       0.88

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     87/100      1.23G     0.4609     0.5058     0.8323         20        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.933      0.984      0.975      0.884

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     88/100      1.23G     0.5101     0.5113     0.8328         42        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.935      0.984      0.974      0.882

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     89/100      1.23G     0.4758     0.5062      0.812          5        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.93      0.984      0.975      0.872

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     90/100      1.23G     0.4489     0.4768     0.8174         13        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.923      0.984      0.976      0.879
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     91/100      1.23G     0.3851     0.8539     0.7514          0        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127       0.93      0.969      0.974      0.877

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     92/100      1.23G     0.4156     0.5336     0.8016          6        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.925      0.974      0.972      0.875

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     93/100      1.23G      0.439     0.5305     0.8073          1        640: 100% ━━━━━━━━━━━━ 12/12 5.3it/s 2.2s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.926      0.981      0.967      0.867

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     94/100      1.23G     0.3962     0.5628     0.7935         28        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127      0.926      0.981      0.967      0.868

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     95/100      1.23G     0.4549     0.4981     0.8061          3        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.924      0.976      0.969       0.87

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     96/100      1.23G     0.4272      0.456     0.8018         22        640: 100% ━━━━━━━━━━━━ 12/12 5.1it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.924      0.976      0.971      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     97/100      1.23G     0.4611     0.4828     0.8212         15        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.6it/s 0.4s
                   all         16        127        0.9      0.994      0.972      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     98/100      1.23G      0.464     0.4716     0.8125         19        640: 100% ━━━━━━━━━━━━ 12/12 5.4it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.904          1      0.973      0.873

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K     99/100      1.23G     0.4462      1.484     0.7413         16        640: 100% ━━━━━━━━━━━━ 12/12 5.2it/s 2.3s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.932      0.967      0.972      0.874

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
[K    100/100      1.23G      0.425     0.4471     0.8156          8        640: 100% ━━━━━━━━━━━━ 12/12 5.5it/s 2.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.907      0.997      0.972      0.875

100 epochs completed in 0.088 hours.
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3\weights\last.pt, 5.3MB
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3\weights\best.pt, 5.3MB

Validating C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3\weights\best.pt...
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
YOLOv5n summary (fused): 84 layers, 2,503,139 parameters, 0 gradients, 7.1 GFLOPs
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.932      0.992       0.98      0.885
Speed: 0.1ms preprocess, 1.3ms inference, 0.0ms loss, 1.0ms postprocess per image
Results saved to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3[0m
Training results: C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLOv5nu-results-3