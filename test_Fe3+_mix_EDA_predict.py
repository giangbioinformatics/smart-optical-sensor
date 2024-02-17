from smartsensor.base import evaluate_metrics, get_data
import joblib

data = get_data(
    rgb_path="EDA/Fe3+_mix/process_data_not_filter/delta_normalized_roi/RGB_values.csv",
    concentration="EDA/Fe3+_mix/concentration.csv",
    outdir="EDA/Fe3+_mix",
)
model = joblib.load(
    "EDA/Fe3+/result_without_filter_and_feature_selection_3_batches_get_fomula/delta_normalized_roi/delta_roi_RGB_model.sav"
)
metric, detail = evaluate_metrics(
    model=model,
    data=data,
    features=["meanR", "meanG", "meanB", "modeR", "modeB", "modeG"],
    degree=1,
)
metric.to_csv("metric.csv", index=False)
detail.to_csv("detail.csv", index=False)
detail[detail["predicted_concentration"] >= 3]
