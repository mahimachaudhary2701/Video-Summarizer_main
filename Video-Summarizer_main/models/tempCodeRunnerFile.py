bg_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG(
    #     history=500, nmixtures=5, backgroundRatio=0.7, noiseSigma=0
    # )