import os
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

restored_dir = r"D:\root\autodl-fs\results\DAIT\Test2800"
gt_dir = r"D:\CPRAformer-main\Datasets\Synthetic_Rain_Datasets\test\Test2800\target"

def main():
    psnr_list = []
    ssim_list = []
    img_names = sorted(os.listdir(restored_dir))

    for name in img_names:
        # 获取不带后缀的文件名
        name_no_ext = os.path.splitext(name)[0]
        restored_path = os.path.join(restored_dir, name)

        # 尝试找同名jpg真值图
        gt_path = os.path.join(gt_dir, f"{name_no_ext}.jpg")
        if not os.path.exists(gt_path):
            print(f"真值图缺失，跳过：{name}")
            continue

        res_img = cv2.imread(restored_path)
        gt_img = cv2.imread(gt_path)
        if res_img is None or gt_img is None:
            print(f"图片读取失败，跳过：{name}")
            continue
        
        if res_img.shape != gt_img.shape:
            h,w = gt_img.shape[:2]
            res_img = cv2.resize(res_img, (w, h))

        res_rgb = cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB)
        gt_rgb = cv2.cvtColor(gt_img, cv2.COLOR_BGR2RGB)

        p = psnr(gt_rgb, res_rgb, data_range=255)
        s = ssim(gt_rgb, res_rgb, channel_axis=2, data_range=255)

        psnr_list.append(p)
        ssim_list.append(s)
        print(f"{name} | PSNR:{p:.2f}, SSIM:{s:.4f}")

    avg_psnr = np.mean(psnr_list)
    avg_ssim = np.mean(ssim_list)
    print("\n======= 2142张有效样本 平均指标 =======")
    print(f"Average PSNR = {avg_psnr:.2f} dB")
    print(f"Average SSIM = {avg_ssim:.4f}")

if __name__ == "__main__":
    main()