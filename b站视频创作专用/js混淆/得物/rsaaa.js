const JSEncrypt = require('node-jsencrypt');

// 公钥
const publicKey = `-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANMGZPlLobHYWoZyMvHD0a6emIjEmtf5Z6Q++VIBRulxsUfYvcczjB0fMVvAnd1douKmOX4G690q9NZ6Q7z/TV8CAwEAAQ==
-----END PUBLIC KEY-----`;

// 要加密的数据
const data = `{"sign":"843dd72bd47fa05482e37e776bf036ac","title":"李佳琦推荐","page":2,"sortType":0,"sortMode":1,"limit":20,"showHot":1,"enhancedSearch":0}`;

// 创建 JSEncrypt 实例
const encryptor = new JSEncrypt();

// 设置公钥
encryptor.setPublicKey(publicKey);

// 加密数据
const encryptedData = encryptor.encrypt(data);

// 打印加密后的数据
console.log(encryptedData);