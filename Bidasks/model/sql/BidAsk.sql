use ant_test_db;

CREATE TABLE bidasks(
    id         INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    code       VARCHAR(10) NOT NULL,
    volume     INT NOT NULL,
    bid        DECIMAL(18, 2) NOT NULL,
    ask        DECIMAL(18, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)CHARSET=utf8;

-- mysql내 명령어 : source test.sql

-- return [code, volume, bid, ask, timestamp] #test

-- # **노드js 모델링 참고**
-- # const Model = require('./lib/Model');

-- # class BidAsk extends Model {
-- #     static tableName = 'ant_bid_asks';
-- #     static timestamp = false;
-- #     static attributes = {
-- #         assetRfId: {
-- #             type: Model.DataTypes.STRING(20),
-- #             primaryKey: true,
-- #         },
-- #         type: {
-- #             type: Model.DataTypes.CHAR(1),
-- #             defaultValue: 'b', // b => bid | a => ask
-- #             primaryKey:true,
-- #         },
-- #         createdAt: {
-- #             type: Model.DataTypes.DATE(),
-- #             primaryKey: true,
-- #             defaultValue: Model.literal('CURRENT_TIMESTAMP()')
-- #         },
-- #         order: {
-- #             type: Model.DataTypes.TINYINT(),
-- #             primaryKey: true,
-- #         },
-- #         marketPrice: {
-- #             type: Model.DataTypes.INTEGER(),
-- #         },
-- #         price: {
-- #             type: Model.DataTypes.INTEGER(),
-- #         },
-- #         volume: {
-- #             type: Model.DataTypes.INTEGER()
-- #         },
-- #         lp: {
-- #             type: Model.DataTypes.INTEGER()
-- #         }
-- #     }
-- # }

-- # module.exports = BidAsk;
