# Project 1 - Ironhack Payments

## Exploratory Data Analysis

Before we can get started with working with the data, we must first perform a data analysis to learn about the data set that we will be working with. The first thing we need to do is use the .head() method to bring
the first few rows of the data set and see the fields and values accordingly.

Running the head() method on the cash requests data set yields:
| id | amount | status   | created_at                  | updated_at                  | user_id | moderated_at              | deleted_account_id | reimbursement_date         | cash_request_received_date | money_back_date | transfer_type | send_at | recovery_status | reco_creation | reco_last_update |
|----|--------|----------|-----------------------------|-----------------------------|---------|---------------------------|--------------------|-----------------------------|----------------------------|-----------------|---------------|--------|-----------------|---------------|------------------|
| 0  | 5      | 100.0    | rejected                   | 2019-12-10 19:05:21.596873 | 2019-12-11 16:47:42.40783  | 804.0   | 2019-12-11 16:47:42.405646 | NaN                 | 2020-01-09 19:05:21.596363 | NaN                        | NaN             | regular       | NaN    | NaN             | NaN           | NaN              |
| 1  | 70     | 100.0    | rejected                   | 2019-12-10 19:50:12.34778  | 2019-12-11 14:24:22.900054 | 231.0   | 2019-12-11 14:24:22.897988 | NaN                 | 2020-01-09 19:50:12.34778  | NaN                        | NaN             | regular       | NaN    | NaN             | NaN           | NaN              |
| 2  | 7      | 100.0    | rejected                   | 2019-12-10 19:13:35.82546  | 2019-12-11 09:46:59.779773 | 191.0   | 2019-12-11 09:46:59.777728 | NaN                 | 2020-01-09 19:13:35.825041 | NaN                        | NaN             | regular       | NaN    | NaN             | NaN           | NaN              |
| 3  | 10     | 99.0     | rejected                   | 2019-12-10 19:16:10.880172 | 2019-12-18 14:26:18.136163 | 761.0   | 2019-12-18 14:26:18.128407 | NaN                 | 2020-01-09 19:16:10.879606 | NaN                        | NaN             | regular       | NaN    | NaN             | NaN           | NaN              |
| 4  | 1594   | 100.0    | rejected                   | 2020-05-06 09:59:38.877376 | 2020-05-07 09:21:55.34008  | 7686.0  | 2020-05-07 09:21:55.320193 | NaN                 | 2020-06-05 22:00:00+00     | NaN                        | NaN             | regular       | NaN    | NaN             | NaN           | NaN              |

Running the head() method on the fees data set yields:
| id | cash_request_id | type            | status   | category               | total_amount | reason                              | created_at                  | updated_at                  | paid_at                     | from_date | to_date | charge_moment |
|----|-----------------|-----------------|----------|------------------------|--------------|-------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------|---------|---------------|
| 0  | 6537           | instant_payment | rejected | NaN                    | 5.0          | Instant Payment Cash Request 14941 | 2020-09-07 10:47:27.42315  | 2020-10-13 14:25:09.396112 | 2020-12-17 14:50:07.47011  | NaN       | NaN     | after         |
| 1  | 6961           | incident        | accepted | rejected_direct_debit  | 5.0          | rejected direct debit              | 2020-09-09 20:51:17.998653 | 2020-10-13 14:25:15.537063 | 2020-12-08 17:13:10.45908  | NaN       | NaN     | after         |
| 2  | 16296          | instant_payment | accepted | NaN                    | 5.0          | Instant Payment Cash Request 23371 | 2020-10-23 10:10:58.352972 | 2020-10-23 10:10:58.352994 | 2020-11-04 19:34:37.43291  | NaN       | NaN     | after         |
| 3  | 20775          | instant_payment | accepted | NaN                    | 5.0          | Instant Payment Cash Request 26772 | 2020-10-31 15:46:53.643958 | 2020-10-31 15:46:53.643982 | 2020-11-19 05:09:22.500223 | NaN       | NaN     | after         |
| 4  | 11242          | instant_payment | accepted | NaN                    | 5.0          | Instant Payment Cash Request 19350 | 2020-10-06 08:20:17.170432 | 2020-10-13 14:25:03.267983 | 2020-11-02 14:45:20.355598 | NaN       | NaN     | after         |

Now that we know the fields we are working with, we notice they are related by id, a parameter we can use to merge them into a more useful set.


