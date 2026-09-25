from scipy.spatial import distance


def find_n_closest(query_vector, embeddings, n=3):
    """计算查询向量与所有 embeddings 的 Cosine Distance，然后按照距离从小到大排序，取最接近的 N 个。"""
    distances = []
    for index, embedding in enumerate(embeddings):
        # Calculate the cosine distance between the query vector and embedding
        dist = distance.cosine(query_vector, embedding)
        # Append the distance and index to distances
        distances.append({"distance": dist, "index": index})

    # Sort distances by the distance key
    distances_sorted = sorted(distances, key=lambda x: x["distance"])

    # Return the first n elements in distances_sorted
    # 距离越小，代表语义越接近
    return distances_sorted[0:n]


# Define a function to combine the relerant features into a single string
def create_product_text(product):
    """把一个商品的结构化数据转换成文本"""
    return f"""
Title: {product["title"]}
Description: {product["short_description"]}
Category: {product["category"]}
Features: {", ".join(product["features"])}
"""
