import pytesseract

# use image_to_data pytesseract method
def image_to_text(out_rgb, lang, config, output_type):
    print(f'run image_to_text., args: out_rgb, lang, config, output_type: {out_rgb, lang, config, output_type}')
    img_data = pytesseract.image_to_data(out_rgb,
                                         lang,
                                         config=config,
                                         output_type=pytesseract.Output.DATAFRAME)
    img_conf_text = img_data[["conf", "text"]]
    img_valid = img_conf_text[img_conf_text["text"].notnull()]
    img_words = img_valid[img_valid["text"].str.len() > 1]

    all_predictions = img_words["text"].to_list()
    print(f'finish image_to_text., returns: {all_predictions}')

    return all_predictions