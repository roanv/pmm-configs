                    elif mdb_item and attribute == "mdb":
                        found_rating = (mdb_item.score - 37) / 5 if mdb_item.score else None
