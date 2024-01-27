from smartsensor.base import *

# Split the images by train test split
def train_test_split_of_all(
    path_of_all: str, rgb_path: str, process_type: str, test_size: float, outdir: str
):
    os.makedirs(outdir, exist_ok=True)

    # data = get_data(rgb_path=rgb_path, concentration=conv_path, outdir=outdir)
    train_set = []
    for batch in path_of_all:
        train = get_data(
            rgb_path=rgb_path, concentration=batch, outdir=outdir
        )
        train_set.append(train)

    if len(train_set) > 1:
        data = pd.concat(train_set, ignore_index=True)
    else:
        data = train_set[0]

    # List of unique concentrations in your DataFrame
    concentrations = data["concentration"].unique()
    # Initialize empty lists to store the splits
    (
        image_train_list,
        image_test_list,
        concentration_train_list,
        concentration_test_list,
    ) = ([], [], [], [])
    # Iterate through each concentration
    for concentration in concentrations:
        # Filter the DataFrame for the current concentration
        subset_conv = data[data["concentration"] == concentration]
        x_data = subset_conv.drop(columns=["concentration"])
        y_data = subset_conv["concentration"]
        (
            image_train,
            image_test,
            concentration_train,
            concentration_test,
        ) = train_test_split(
            x_data,
            y_data,
            test_size=test_size,
            random_state=42,
        )

        # Append the splits to the lists
        image_train_list.append(image_train)
        image_test_list.append(image_test)
        concentration_train_list.append(concentration_train)
        concentration_test_list.append(concentration_test)

    # Concatenate the splits to obtain the final training and testing sets
    final_image_train = pd.concat(image_train_list)
    final_image_test = pd.concat(image_test_list)
    final_concentration_train = pd.concat(concentration_train_list)
    final_concentration_test = pd.concat(concentration_test_list)
    # Create the final training and testing sets
    final_train_data = pd.concat([final_image_train, final_concentration_train], axis=1)
    final_test_data = pd.concat([final_image_test, final_concentration_test], axis=1)
    # Save the training and testing sets
    train_path = os.path.join(outdir, f"{process_type}_train.csv")
    test_path = os.path.join(outdir, f"{process_type}_test.csv")
    final_train_data.to_csv(train_path, index=False)
    final_test_data.to_csv(test_path, index=False)
    return final_train_data, final_test_data, train_path, test_path


def end2end_model(
    train_rgb_path: str,
    train_concentration: list,
    test_rgb_path: str,
    test_concentration: str,
    features: str,
    degree: int,
    outdir: str,
    prefix: str,
    skip_feature_selection: bool = True,
    test_size: float = 0.3,
):
    # Load data
    if test_concentration is None or test_rgb_path is None:
        train, test, train_path, test_path = train_test_split_of_all(
            path_of_all=train_concentration,
            rgb_path=train_rgb_path,
            process_type=prefix,
            test_size=test_size,
            outdir=outdir,
        )
    else:
        # combine multi batches
        train_set = []
        for batch in train_concentration:
            train = get_data(
                rgb_path=train_rgb_path, concentration=batch, outdir=outdir
            )
            train_set.append(train)

        if len(train_set) > 1:
            train = pd.concat(train_set, ignore_index=True)
        else:
            train = train_set[0]

        test = get_data(
            rgb_path=test_rgb_path, concentration=test_concentration, outdir=outdir
        )
    # Train
    features = features.split(",")
    train_model, selected_features = train_regression(
        train=train,
        features=features,
        degree=degree,
        outdir=outdir,
        prefix=prefix,
        skip_feature_selection=skip_feature_selection,
    )
    # Evaluate
    train_metric, train_detail = evaluate_metrics(
        model=train_model,
        data=train,
        features=selected_features,
        degree=degree,
    )
    test_metric, test_detail = evaluate_metrics(
        model=train_model,
        data=test,
        features=selected_features,
        degree=degree,
    )

    train_temps = []
    if test_concentration is None or test_rgb_path is None:
        for batch in train_concentration:
            train_temps.append(f"{os.path.basename(batch).split('.')[0]}_by_split_{test_size}")
        test_dataset = f"{os.path.basename(batch).split('.')[0]}_by_split_{test_size}"
    else:
        for batch in train_concentration:
            train_temps.append(f"{os.path.basename(batch).split('.')[0]}")
        test_dataset = f"{os.path.basename(test_concentration).split('.')[0]}"
    train_dataset = "_".join(train_temps)
    # train res
    train_metric["train_data"] =  train_dataset
    train_metric["test_data"] = train_dataset
    train_detail["train_data"] = train_dataset
    train_detail["test_data"] = train_dataset
    # test res
    test_metric["train_data"] = train_dataset
    test_metric["test_data"] = test_dataset
    test_detail["train_data"] = train_dataset
    test_detail["test_data"] = test_dataset

    train_metric["features"] = ",".join(selected_features)
    test_metric["features"] = ",".join(selected_features)
    metric = pd.concat([train_metric, test_metric], axis=0)
    detail = pd.concat([train_detail, test_detail], axis=0)
    # Export data
    metric_path = os.path.join(outdir, f"metric_train_{train_dataset}_test_{test_dataset}.csv")
    detail_path = os.path.join(outdir, f"detail_train_{train_dataset}_test_{test_dataset}.csv")
    metric.to_csv(metric_path, index=False)
    detail.to_csv(detail_path, index=False)
    return metric, detail

