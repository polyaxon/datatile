// Copyright 2018-2021 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.6.1
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * V1ArtifactTree
 */

public class V1ArtifactTree {
  public static final String SERIALIZED_NAME_FILES = "files";
  @SerializedName(SERIALIZED_NAME_FILES)
  private Map<String, String> files = null;

  public static final String SERIALIZED_NAME_DIRS = "dirs";
  @SerializedName(SERIALIZED_NAME_DIRS)
  private List<String> dirs = null;

  public static final String SERIALIZED_NAME_IS_DONE = "is_done";
  @SerializedName(SERIALIZED_NAME_IS_DONE)
  private Boolean isDone;


  public V1ArtifactTree files(Map<String, String> files) {
    
    this.files = files;
    return this;
  }

  public V1ArtifactTree putFilesItem(String key, String filesItem) {
    if (this.files == null) {
      this.files = new HashMap<String, String>();
    }
    this.files.put(key, filesItem);
    return this;
  }

   /**
   * Get files
   * @return files
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Map<String, String> getFiles() {
    return files;
  }


  public void setFiles(Map<String, String> files) {
    this.files = files;
  }


  public V1ArtifactTree dirs(List<String> dirs) {
    
    this.dirs = dirs;
    return this;
  }

  public V1ArtifactTree addDirsItem(String dirsItem) {
    if (this.dirs == null) {
      this.dirs = new ArrayList<String>();
    }
    this.dirs.add(dirsItem);
    return this;
  }

   /**
   * Get dirs
   * @return dirs
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getDirs() {
    return dirs;
  }


  public void setDirs(List<String> dirs) {
    this.dirs = dirs;
  }


  public V1ArtifactTree isDone(Boolean isDone) {
    
    this.isDone = isDone;
    return this;
  }

   /**
   * Get isDone
   * @return isDone
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getIsDone() {
    return isDone;
  }


  public void setIsDone(Boolean isDone) {
    this.isDone = isDone;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1ArtifactTree v1ArtifactTree = (V1ArtifactTree) o;
    return Objects.equals(this.files, v1ArtifactTree.files) &&
        Objects.equals(this.dirs, v1ArtifactTree.dirs) &&
        Objects.equals(this.isDone, v1ArtifactTree.isDone);
  }

  @Override
  public int hashCode() {
    return Objects.hash(files, dirs, isDone);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1ArtifactTree {\n");
    sb.append("    files: ").append(toIndentedString(files)).append("\n");
    sb.append("    dirs: ").append(toIndentedString(dirs)).append("\n");
    sb.append("    isDone: ").append(toIndentedString(isDone)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

