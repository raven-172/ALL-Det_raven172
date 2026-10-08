YOLO26n summary: 260 layers, 2,572,280 parameters, 0 gradients, 6.2 GFLOPs
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
[34m[1mengine\trainer: [0magnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=8, bgr=0.0, box=7.5, cache=False, cfg=None, channels_last=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, cls_remap=True, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dgrad=0.5, dis=6.0, distill_model=None, dlam=1.0, dlog=1.0, dnn=False, dropout=0.0, dynamic=False, embed=None, epochs=100, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, iou=0.7, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolo26n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=YOLO26-result, nbs=64, nms=None, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results, quantize=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=42, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=tracktrack.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=0, workspace=None
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
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5, 3, True]        
 10                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    119808  ultralytics.nn.modules.block.C3k2            [384, 128, 1, True]           
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1     34304  ultralytics.nn.modules.block.C3k2            [256, 64, 1, True]            
 17                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1     95232  ultralytics.nn.modules.block.C3k2            [192, 128, 1, True]           
 20                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1    463104  ultralytics.nn.modules.block.C3k2            [384, 256, 1, True, 0.5, True]
 23        [16, 19, 22]  1    241566  ultralytics.nn.modules.head.Detect           [1, 1, True, [64, 128, 256]]  
YOLO26n summary: 260 layers, 2,504,190 parameters, 2,504,190 gradients, 5.9 GFLOPs

Transferred 606/708 items from pretrained weights
[34m[1mAMP: [0mrunning Automatic Mixed Precision (AMP) checks...
[34m[1mAMP: [0mchecks passed 
[34m[1mtrain: [0mFast image access  (ping: 0.00.0 ms, read: 2098.4266.7 MB/s, size: 1173.3 KB)
[K[34m[1mtrain: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\train.cache... 91 images, 49 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 91/91  0.0s
[34m[1mval: [0mFast image access  (ping: 0.00.0 ms, read: 2450.3208.4 MB/s, size: 1271.6 KB)
[K[34m[1mval: [0mScanning C:\Users\ezycloudx-admin\Desktop\LVHH\ALL_IDB1\ALL_IDB1_splitted\labels\val.cache... 16 images, 9 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 16/16  0.0s
[34m[1moptimizer:[0m 'optimizer=auto' found, ignoring 'lr0=0.01' and determining best 'optimizer' and 'lr0' automatically... 
[34m[1moptimizer:[0m AdamW(lr=0.002, momentum=0.9) with parameter groups 114 weight(decay=0.0), 126 weight(decay=0.0005), 126 bias(decay=0.0)
Plotting labels to C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result\labels.jpg... 
Using 91 train, 16 val images for fraction=1.0 at imgsz=640
Using 0 dataloader workers
Logging results to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result[0m
Starting training for 100 epochs...

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      1/100      1.38G      1.077      5.017   0.003173         17        640: 100% ━━━━━━━━━━━━ 12/12 2.7it/s 4.4s0.4s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0133      0.504     0.0116    0.00726

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      2/100      1.54G      1.004      4.688   0.002723         36        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127     0.0229      0.866     0.0488     0.0304

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      3/100      1.54G      1.042      3.737   0.002999         33        640: 100% ━━━━━━━━━━━━ 12/12 4.1it/s 3.0s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127     0.0262      0.992     0.0377     0.0238

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      4/100      1.54G      1.166      3.658   0.003451         23        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127     0.0262      0.992      0.582      0.318

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      5/100      1.54G     0.9777      3.179   0.003134         14        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.752      0.465      0.763      0.573

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      6/100      1.54G     0.8376      3.153   0.002403          9        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.797      0.772      0.828      0.629

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      7/100      1.54G     0.8915      3.349   0.002735          5        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.821      0.936      0.924      0.765

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      8/100      1.54G     0.7489      3.394   0.002335         24        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.837      0.906       0.94      0.663

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K      9/100      1.54G     0.8193      2.875   0.002643         12        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.802      0.957      0.938      0.765

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     10/100      1.54G     0.8855      5.853   0.003011         23        640: 100% ━━━━━━━━━━━━ 12/12 3.8it/s 3.2s0.3s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127      0.839      0.898      0.911      0.731

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     11/100      1.54G     0.7874      2.399   0.002018          8        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.829      0.898      0.914       0.76

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     12/100      1.54G     0.9173      2.266    0.00279         12        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.837      0.929      0.932      0.779

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     13/100      1.54G     0.8299      2.359   0.002445         25        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.824      0.956      0.939      0.771

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     14/100      1.54G     0.8086      2.171   0.002231         21        640: 100% ━━━━━━━━━━━━ 12/12 4.1it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.863      0.893      0.936      0.801

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     15/100      1.54G     0.8443      3.828   0.002612          1        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.868      0.935      0.951      0.776

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     16/100      1.54G     0.7982      1.865   0.002178         28        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.871      0.954      0.955      0.762

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     17/100      1.54G     0.7313      2.021   0.002132         16        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.869       0.94       0.96      0.809

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     18/100      1.54G     0.6998      2.702   0.002175         41        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.85      0.913      0.948      0.782

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     19/100      1.54G     0.8147      2.311   0.002296         14        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.916      0.827       0.91      0.775

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     20/100      1.54G     0.7786      1.998   0.001904         32        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.895      0.877      0.948      0.809

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     21/100      1.54G     0.7544      1.722   0.002156         63        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.86      0.968      0.954      0.823

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     22/100      1.54G     0.6998      2.162   0.002018          5        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.852      0.949      0.959      0.834

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     23/100      1.54G     0.7043      1.643   0.002002         27        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.874      0.875      0.958       0.75

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     24/100      1.54G     0.7404      1.588   0.002204         16        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.849      0.945      0.959      0.766

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     25/100      1.54G     0.7358      1.604   0.002046         28        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.881      0.969      0.962      0.855

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     26/100      1.54G     0.7256      1.394   0.001714         32        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.88      0.969      0.964      0.827

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     27/100      1.54G     0.6787      2.385   0.002184          4        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.891      0.913      0.957      0.833

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     28/100      1.54G     0.6246      1.846   0.001827          8        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.887      0.882       0.95      0.801

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     29/100      1.54G     0.6565      1.541   0.002033         15        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.849      0.969      0.968      0.865

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     30/100      1.54G     0.6493      1.407   0.001893          9        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.892      0.921      0.968      0.857

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     31/100      1.54G     0.6608      1.482   0.001896         34        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.926      0.885      0.969      0.853

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     32/100      1.54G     0.6739      1.637   0.001894          2        640: 100% ━━━━━━━━━━━━ 12/12 4.0it/s 3.0s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.896      0.898      0.966      0.868

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     33/100      1.54G     0.7039      1.389   0.001969         19        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.85      0.945      0.959      0.838

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     34/100      1.54G     0.6271      1.635   0.001765         11        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.858      0.952      0.963      0.834

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     35/100      1.54G     0.6524      1.285   0.001977         14        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127       0.89      0.953      0.976      0.876

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     36/100      1.54G     0.6228      1.251   0.001887          8        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.909      0.944      0.978      0.873

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     37/100      1.54G     0.6223      1.551   0.001781         29        640: 100% ━━━━━━━━━━━━ 12/12 4.0it/s 3.0s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.932      0.937      0.977      0.867

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     38/100      1.54G     0.6316      1.083   0.001749          9        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.94      0.921      0.977      0.877

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     39/100      1.54G     0.6095      1.097   0.001786         19        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.959      0.911       0.98      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     40/100      1.54G     0.6507      1.039   0.001825         34        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.896      0.969       0.98      0.877

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     41/100      1.54G     0.6488      1.557   0.001824          1        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.895      0.942      0.974      0.857

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     42/100      1.54G     0.6088     0.9711   0.001827         18        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.897      0.959      0.978      0.872

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     43/100      1.54G       0.65     0.9789   0.001874         44        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.969      0.982      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     44/100      1.54G     0.6483      1.063   0.001734         17        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.923      0.948       0.98      0.887

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     45/100      1.54G     0.6331     0.9698   0.001759         23        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.3s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.903      0.961      0.982      0.874

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     46/100      1.54G     0.6168      1.117   0.001917         21        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.881      0.991      0.982      0.883

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     47/100      1.54G     0.6457     0.9673   0.001882         12        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.898      0.968       0.98      0.861

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     48/100      1.54G     0.5982      1.058   0.001664          3        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.917      0.953       0.98      0.878

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     49/100      1.54G     0.5755      1.033    0.00182         17        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.898      0.976      0.977      0.887

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     50/100      1.54G     0.5996     0.8342   0.001617          8        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.898      0.967      0.976       0.87

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     51/100      1.54G       0.64     0.8884   0.001724         15        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.923      0.942      0.976      0.869

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     52/100      1.54G     0.6189      1.072   0.001791          9        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.913      0.953      0.979      0.881

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     53/100      1.54G     0.6069     0.9079   0.001637         16        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.906      0.984      0.979      0.891

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     54/100      1.54G     0.6536     0.9108   0.002159         13        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.905      0.976      0.977       0.89

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     55/100      1.54G     0.5755     0.8521   0.001687         10        640: 100% ━━━━━━━━━━━━ 12/12 4.7it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.899      0.983      0.979      0.891

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     56/100      1.54G     0.5598     0.8972   0.001521         24        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.925      0.972      0.982      0.887

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     57/100      1.54G     0.5523     0.7881   0.001563         16        640: 100% ━━━━━━━━━━━━ 12/12 4.0it/s 3.0s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.936      0.992      0.985       0.89

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     58/100      1.54G     0.5849     0.7388   0.001598         11        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127       0.94      0.983      0.985      0.863

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     59/100      1.54G     0.6663     0.7476   0.001847         15        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.937      0.984      0.985      0.889

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     60/100      1.54G     0.6076      1.019   0.001892          9        640: 100% ━━━━━━━━━━━━ 12/12 4.1it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.939      0.984      0.986        0.9

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     61/100      1.54G     0.6034     0.7285   0.001647         53        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.938      0.992      0.986      0.903

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     62/100      1.54G     0.6022     0.7311    0.00187         20        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.928      0.984      0.986      0.899

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     63/100      1.54G      0.604     0.6527   0.001697         12        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.93      0.969      0.984      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     64/100      1.54G     0.5859     0.7333    0.00163         32        640: 100% ━━━━━━━━━━━━ 12/12 4.0it/s 3.0s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.906      0.992      0.982      0.887

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     65/100      1.54G     0.5602      0.718    0.00156         17        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.893      0.992      0.978      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     66/100      1.54G     0.5841       0.76   0.001578          7        640: 100% ━━━━━━━━━━━━ 12/12 4.1it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.893      0.983      0.977      0.885

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     67/100      1.54G     0.5378     0.7096   0.001616         21        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.922      0.927      0.973      0.877

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     68/100      1.54G     0.5529     0.6841   0.001673         10        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.918      0.929      0.974      0.883

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     69/100      1.54G     0.5418     0.7465   0.001648         29        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127        0.9      0.989      0.977      0.886

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     70/100      1.54G     0.5861     0.7457   0.001859         24        640: 100% ━━━━━━━━━━━━ 12/12 4.1it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.906      0.969      0.979      0.887

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     71/100      1.54G     0.5861      0.626   0.001493         11        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.899      0.984      0.979      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     72/100      1.54G     0.5351     0.6568   0.001608         39        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.898      0.973       0.98      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     73/100      1.54G     0.6095     0.6299   0.001641         45        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.904      0.963      0.979      0.894

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     74/100      1.54G     0.5984     0.6969    0.00181         32        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.1it/s 0.5s
                   all         16        127      0.891       0.97      0.978      0.895

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     75/100      1.54G     0.5364     0.6572   0.001518         10        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.929      0.927      0.976      0.889

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     76/100      1.54G     0.5573     0.6569   0.001627         11        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127       0.93      0.936      0.977      0.895

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     77/100      1.54G     0.5957     0.6807   0.001623          6        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.928      0.961      0.981      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     78/100      1.54G     0.6933      1.061   0.001826          1        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.931      0.957      0.981      0.889

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     79/100      1.54G     0.5449     0.8037   0.001747         10        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.924      0.964      0.982      0.894

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     80/100      1.54G     0.5254     0.5918   0.001425          8        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.924      0.953      0.982      0.902

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     81/100      1.54G     0.5567     0.6277   0.001509         11        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.926      0.969      0.982      0.906

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     82/100      1.54G     0.5295     0.5822   0.001474         13        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.929      0.969      0.982      0.901

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     83/100      1.54G     0.5461     0.5922   0.001548         34        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.931       0.96      0.981      0.902

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     84/100      1.54G     0.5818     0.6438   0.001722         30        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.932      0.965      0.981      0.899

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     85/100      1.54G     0.5892     0.6414   0.001693         35        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.937      0.961      0.981      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     86/100      1.54G     0.5728     0.6389   0.001596         32        640: 100% ━━━━━━━━━━━━ 12/12 3.8it/s 3.2s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.935      0.961      0.981      0.899

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     87/100      1.54G     0.5204     0.7058   0.001489         20        640: 100% ━━━━━━━━━━━━ 12/12 4.3it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.936      0.953      0.979      0.903

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     88/100      1.54G     0.5552     0.6156   0.001487         42        640: 100% ━━━━━━━━━━━━ 12/12 4.2it/s 2.9s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.937      0.943      0.979      0.905

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     89/100      1.54G     0.5541     0.6392   0.001569          5        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.935      0.937      0.979      0.903

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     90/100      1.54G     0.4989     0.6776   0.001424         13        640: 100% ━━━━━━━━━━━━ 12/12 4.4it/s 2.8s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.915      0.961      0.979        0.9
Closing dataloader mosaic

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     91/100      1.54G     0.4331     0.8817   0.001679          0        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127       0.91      0.954      0.979      0.899

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     92/100      1.54G     0.4996     0.7551   0.001823          6        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.906      0.976      0.979      0.898

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     93/100      1.54G     0.5135     0.8756   0.001656          1        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.5s
                   all         16        127      0.912      0.974       0.98      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     94/100      1.54G     0.5014      1.149   0.001806         28        640: 100% ━━━━━━━━━━━━ 12/12 4.6it/s 2.6s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.912      0.975      0.981      0.892

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     95/100      1.54G     0.4765     0.7194   0.001404          3        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.912      0.974       0.98      0.889

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     96/100      1.54G      0.461     0.6333   0.001467         22        640: 100% ━━━━━━━━━━━━ 12/12 4.5it/s 2.7s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.912      0.975       0.98       0.89

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     97/100      1.54G     0.5535     0.7225   0.001929         15        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.4it/s 0.4s
                   all         16        127      0.912      0.975       0.98      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     98/100      1.54G     0.4863     0.6596    0.00155         19        640: 100% ━━━━━━━━━━━━ 12/12 4.9it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.912      0.975       0.98      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K     99/100      1.54G     0.4619      1.151   0.001377         16        640: 100% ━━━━━━━━━━━━ 12/12 5.0it/s 2.4s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.5it/s 0.4s
                   all         16        127      0.911      0.976       0.98      0.897

      Epoch    GPU_mem   box_loss   cls_loss    l1_loss  Instances       Size
[K    100/100      1.54G     0.4688     0.6958   0.001524          8        640: 100% ━━━━━━━━━━━━ 12/12 4.8it/s 2.5s0.2s
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.2it/s 0.4s
                   all         16        127      0.912      0.975       0.98      0.894

100 epochs completed in 0.099 hours.
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result\weights\last.pt, 5.4MB
Optimizer stripped from C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result\weights\best.pt, 5.4MB

Validating C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result\weights\best.pt...
Ultralytics 8.4.174  Python-3.12.10 torch-2.13.0+cu130 CUDA:0 (NVIDIA GeForce RTX 5060 Ti, 16311MiB)
YOLO26n summary (fused): 120 layers, 2,375,031 parameters, 0 gradients, 5.3 GFLOPs
[K                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 1/1 2.3it/s 0.4s
                   all         16        127      0.925      0.969      0.983      0.903
Speed: 0.1ms preprocess, 1.6ms inference, 0.0ms loss, 1.4ms postprocess per image
Results saved to [1mC:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result[0m
Training results: C:\Users\ezycloudx-admin\Desktop\ALL-Det_raven172_processing\results\RES001_EXP001-results\YOLO26-results\YOLO26-result