pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Traceability {

    struct ProductInfo {
        string dateTime;
        address passedObject;
        string verifier;
    }

    struct ObjectInfo {
        string name;
        string phoneNumber;
        string website;
        string category;
        string objectAddress;  // 修改字段名称以避免冲突
        string description;
    }

    // Mapping from account address to Objects
    mapping(address => ObjectInfo) public Objects;

    // Mapping from product ID to Product array
    mapping(string => ProductInfo[]) public products;

    function createProduct(string memory _id, string memory _dateTime, address _passedObject, string memory _verifier) public {
        require(products[_id].length == 0, "Product ID already exists");
        products[_id].push(ProductInfo(_dateTime, _passedObject, _verifier));
    }

    function transferProduct(string memory _id, string memory _dateTime, address _passedObject, string memory _verifier) public {
        require(products[_id].length > 0, "Product does not exist");
        ProductInfo memory lastProduct = products[_id][products[_id].length - 1];
        require(msg.sender == lastProduct.passedObject, "Only the owner of the product can transfer it");

        products[_id].push(ProductInfo(_dateTime, _passedObject, _verifier));
    }

    function getProduct(string memory _id) public view returns (ProductInfo[] memory) {
        return products[_id];
    }

    function createObject(string memory _name, string memory _phoneNumber, string memory _website, string memory _category, string memory _objectAddress, string memory _description) public {
        require(bytes(Objects[msg.sender].name).length == 0, "Object already exists");
        Objects[msg.sender] = ObjectInfo(_name, _phoneNumber, _website, _category, _objectAddress, _description);
    }

    function getObject(address _address) public view returns (string memory, string memory, string memory, string memory, string memory, string memory) {
        require(bytes(Objects[_address].name).length > 0, "Object does not exist");
        ObjectInfo memory obj = Objects[_address];
        return (obj.name, obj.phoneNumber, obj.website, obj.category, obj.objectAddress, obj.description);
    }
}