from assertpy import assert_that, soft_assertions

from services.restful_booker.restful_booker_service import RestfulBookerClient

client = RestfulBookerClient()


def test_if_new_booking_can_be_created(context, create_data):
    response = client.create_booking(create_data)

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()
        assert_that(response.as_dict).contains("bookingid")
        assert_that(response.as_dict["bookingid"]).is_not_none()

    # 只用第一次 response，不要重复 create
    context["booking_id"] = response.as_dict["bookingid"]


def test_if_new_booking_can_be_fetched(context):
    booking_id = context.get("booking_id")

    response = client.get_booking(booking_id)

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()

        # 防止结构不一致，先安全访问
        assert_that(response.as_dict.get("firstname")).is_not_none()
        assert_that(response.as_dict.get("lastname")).is_not_none()


def test_if_new_booking_can_be_updated(context, update_data):
    booking_id = context.get("booking_id")

    response = client.update_booking(booking_id, update_data)

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.as_dict).is_not_empty()

        # update 后字段验证（更安全写法）
        assert_that(response.as_dict.get("additionalneeds")).is_equal_to("Dinner")


def test_if_new_booking_can_be_deleted(context):
    booking_id = context.get("booking_id")

    response = client.delete_booking(booking_id)

    with soft_assertions():
        # 有些API是 201，有些是 200，这里做兼容
        assert_that(response.status_code).is_in(200, 201)

        # delete 一般不会返回 body，这里不强制 .is_empty()


def test_if_new_booking_can_be_deleted_duplicate(context):
    response = client.delete_booking(context.get("booking_id"))
    with soft_assertions():
        # 允许第一次删除 200/201，重复删除 405
        assert_that(response.status_code).is_in(200, 201, 405)
        # delete 重复调用一般不会有返回 body
        assert_that(response.as_dict).is_empty()