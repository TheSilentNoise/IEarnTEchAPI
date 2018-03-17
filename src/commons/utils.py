import json


def convert_to_json(rows, column_names):
    """convert_to_json.

    Converts all the rows in json using column names.
    """
    result = []
    for i in rows:
        result.append(dict(zip(column_names, i)))
    json_string = json.dumps(result, sort_keys=True, indent=4)
    return json.loads(json_string)


def return_result(result=[], error=None, error_code=None):
    return_result = {}

    return_result.update(
        {
            "data": result,
            "error": {
                "code": error_code,
                "message": error
            }
        }
    )

    return_result = json.dumps(return_result)
    return json.loads(return_result)


def return_result_list(result=[], error=None, error_code=None):
    return_result_list = {}

    return_result_list.update(
        {
            "data": result,
            "total_count": len(result),
            "error": {
                "code": error_code,
                "message": error
            }
        }
    )

    return_result_list = json.dumps(return_result_list)
    return json.loads(return_result_list)


def return_result_delete(result={}, error=None, error_code=None):
    return_result_list = {}

    return_result_list.update(
        {
            "data": result,
            "records_effected": 1,
            "error": {
                "code": error_code,
                "message": error
            }
        }
    )

    return_result_list = json.dumps(return_result_list)
    return json.loads(return_result_list)


def get_url_args(req):
    """
    """
    limit = req.args.get("limit", "0")
    offset = req.args.get("offset", "0")
    sort_key = req.args.get("sort", "")
    projection = req.args.get("projection", "BASIC")

    sort_key = sort_key.split(",") if ',' in sort_key else [sort_key]
    return limit, offset, sort_key, projection


def exclude_column_names(column_names=[], exclude_list=[]):
    for col in exclude_list:
        if col:
            column_names.remove(col)
    return column_names


def exclude_entry_dict(passing_dict={}, exclude_list=[]):
    for col in exclude_list:
        if col:
            del passing_dict[col]
    return passing_dict
